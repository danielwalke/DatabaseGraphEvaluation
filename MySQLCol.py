from Data import Data
import numpy as np
from Subgraph import Subgraph
import time
from MySQLQuery import MySQLQuery
from MySQLConnector import MySQLConnector
import json

class MySQLCol(MySQLQuery, MySQLConnector):
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name, max_hops = 3):
        MySQLQuery.__init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        self.intialize_column_data(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        self.initialize_all_queries(max_hops)
        super(MySQLConnector, self).__init__()
        self.db_name = self.X_and_y_file_name.split(".")[0].lower()
        self.session = None

    @staticmethod
    def file_suffix():
        return "col"

    @staticmethod
    def db_name():
        return "mysql"

    def create(self):
        conn = self.connect()
        start = time.time()
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(self.create_db_query % self.db_name)
        conn = self.connect(self.db_name)
        conn.autocommit = True
        self.session = conn.cursor()
        self.session.execute(self.create_nodes_table_query)
        self.session.execute(self.create_edges_table_query)
        self.session.execute(self.create_nodes_query, (f"syn_data/{self.X_and_y_file_name}",))
        self.session.execute(self.create_node_id_index_query)
        self.session.execute(self.create_edges_query, (f"syn_data/{self.edge_file_name}",))
        for query in self.create_edge_index_queries:
            self.session.execute(query)
        return time.time() - start
            
    def read(self, seed_node_id, hops):
        start = time.time()
        self.session.execute(self.group_concat_max_query)
        self.session.execute(self.allowed_packet_max_query)
        self.session.execute(self.read_subgraph_query_dict[hops] %  seed_node_id)
        results = self.session.fetchall()[0]
        if None in results: return None, None
                
        labels = np.array(json.loads(results[1]))
        subgraph_node_features = np.array(json.loads(results[0]))
        subgraph_edges = np.array(json.loads(results[2])).transpose()
        node_ids = np.array(json.loads(results[-1]))
        id_sort_idx = np.argsort(node_ids)
        node_ids = node_ids[id_sort_idx]
        features = subgraph_node_features[id_sort_idx]
        labels = labels[id_sort_idx]
        cols_source = np.searchsorted(node_ids, subgraph_edges[0])
        cols_target = np.searchsorted(node_ids, subgraph_edges[1])
        remapped_edge_index = np.concatenate([np.expand_dims(cols_source, axis = 0), np.expand_dims(cols_target, axis = 0)], axis = 0)
        read_time = time.time() - start    
        return read_time, Subgraph(features = features, labels = labels, edge_index = remapped_edge_index, node_ids = node_ids)
    
    def update_nodes(self, node_id):
        start = time.time()
        self.session.execute(self.update_nodes_query % node_id)
        update_time = time.time() - start
        return update_time
    
    def update_edges(self, selected_edge, new_target_id):
        start = time.time()
        source_id, target_id = selected_edge
        self.session.execute(self.update_edges_query % (new_target_id, int(source_id), int(target_id)))
        return time.time() - start
        
    
    def delete(self):
        start = time.time()
        self.close_session()
        conn = self.connect()
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(self.delete_query % self.db_name)
        conn.close() 
        return time.time() - start

    def close_session(self):
        self.session.close()
        self.conn.close()