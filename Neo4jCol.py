from Data import Data
import numpy as np
from Subgraph import Subgraph
import time
from Neo4jQuery import Neo4jQuery
from Neo4jConnector import Neo4jConnector

class Neo4jCol(Neo4jQuery, Neo4jConnector):
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name, max_hops = 3):
        Neo4jQuery.__init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        self.intialize_column_data(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        self.initialize_all_queries_columns(max_hops)
        super(Neo4jConnector, self).__init__()
        self.connect()
        self.session = self.driver.session()
        self.connect()

    @staticmethod
    def file_suffix():
        return "col"

    @staticmethod
    def db_name():
        return "neo4j"

    def create(self):
        start = time.time()
        # self.session.run(self.create_nodes_query, file=f"file:///{self.X_and_y_file_name}")
        # self.session.run(self.create_node_id_index_query)
        # self.session.run(self.create_edges_query, file=f"file:///{self.edge_file_name}")
        self.session.run(self.create_nodes_query, file=f"file:///home/dwalke/git/db_eval/syn_data/{self.X_and_y_file_name}")
        self.session.run(self.create_node_id_index_query)
        self.session.run(self.create_edges_query, file=f"file:///home/dwalke/git/db_eval/syn_data/{self.edge_file_name}")
        return time.time() - start
            
    def read(self, seed_node_id, hops):
        start = time.time()
        results = self.session.run(self.read_subgraph_query_dict[hops], seed_node_id = seed_node_id)
        res_df = results.to_df()
        if len(res_df["edges"][0]) == 0: return None, None
            
        subgraph_edge_index = np.array(res_df["edges"][0]).transpose()        
        node_ids = np.array(res_df["idCollection"][0])
        sort_idx = np.argsort(node_ids, axis = -1)
        node_ids = node_ids[sort_idx]
        cols_source = np.searchsorted(node_ids, subgraph_edge_index[0])
        cols_target = np.searchsorted(node_ids, subgraph_edge_index[1])
        remapped_edge_index = np.concatenate([np.expand_dims(cols_source, axis = 0), np.expand_dims(cols_target, axis = 0)], axis = 0)
        features = np.array(res_df["features"][0])[sort_idx]
        labels = np.array(res_df["labels"][0])[sort_idx]
        read_time = time.time() - start    
        return read_time, Subgraph(features = features, labels = labels, edge_index = remapped_edge_index, node_ids = node_ids)
    
    def update_nodes(self, node_id):
        start = time.time()
        self.session.run(self.update_nodes_query, node_id=node_id)
        update_time = time.time() - start
        return update_time
    
    def update_edges(self, selected_edge, new_target_id):
        start = time.time()
        source_id, target_id = selected_edge
        self.session.run(self.update_edges_query,
                    source_id=int(source_id),
                    target_id=int(target_id),
                    new_target_id=new_target_id)
        return time.time() - start
        
    
    def delete(self):
        start = time.time()
        self.session.run(self.delete_query)
        self.close_session()
        self.driver.close()
        return time.time() - start

    def close_session(self):
        self.session.close()