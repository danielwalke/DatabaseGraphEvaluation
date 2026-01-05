import numpy as np
import time
import os
import subprocess
from Subgraph import Subgraph
from SQLiteQuery import SQLiteQuery
from SQLiteConnector import SQLiteConnector

class SQLiteCol(SQLiteQuery, SQLiteConnector):
    """
    Manages CRUD operations for a column-based SQLite database.
    It uses the fast .import shell command for initial data creation.
    """
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name, max_hops=3):
        # Initialize query and data loading functionalities
        SQLiteQuery.__init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        self.intialize_column_data(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        self.initialize_all_queries(max_hops)
        
        # Initialize connection functionalities
        super(SQLiteConnector, self).__init__()
        
        # Set database name based on input files
        self.db_name = f"db/{self.X_and_y_file_name.split('.')[0]}_col.db"
        self.session = None
        self.conn = None

    @staticmethod
    def file_suffix():
        return "col"

    @staticmethod
    def db_name():
        return "sqlite"

    def create(self):
        """
        Creates and populates the database.
        It uses the sqlite3 shell's .import command for maximum speed by piping the
        CSV content while skipping the header row.
        """
        start = time.time()

        # Ensure a clean slate by removing the old DB file
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

        # 1. Create the database and tables with the correct schema

        self.conn = self.connect(self.db_name)
        self.session = self.conn.cursor()
        self.session.execute(self.create_nodes_table_query)
        self.session.execute(self.create_edges_table_query)
        self.conn.commit()
        self.conn.close()

        # 2. Use subprocess for fast CSV import, skipping the header
        nodes_path = os.path.join("syn_data", self.X_and_y_file_name)
        edges_path = os.path.join("syn_data", self.edge_file_name)

        abs_nodes_path = os.path.abspath(nodes_path)
        abs_edges_path = os.path.abspath(edges_path)

        # The sqlite3 shell script to run.
        # `tail -n +2` is a POSIX command that outputs the file starting from the
        # second line, effectively skipping the header. This prevents the
        # "datatype mismatch" error.
        import_script = f"""
.mode csv
.separator ","
.import "| tail -n +2 '{abs_nodes_path}'" nodes
.import "| tail -n +2 '{abs_edges_path}'" edges
"""
        try:
            subprocess.run(
                f'sqlite3 "{self.db_name}"',
                input=import_script,
                text=True,
                check=True,
                shell=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Error during bulk import: {e}")
            print("Please ensure sqlite3 and shell commands like 'tail' are available.")
            raise

        # 3. Re-connect to create indices. Header cleanup is no longer needed.
        self.conn = self.connect(self.db_name)
        self.session = self.conn.cursor()
        
        # 4. Create indices for performance
        self.session.execute(self.create_node_id_index_query)
        for query in self.create_edge_index_queries:
            self.session.execute(query)
        self.conn.commit()
        return time.time() - start
            
    def read(self, seed_node_id, hops):
        """Reads a k-hop subgraph, processes the result, and returns a Subgraph object."""
        start = time.time()
               
        self.session.execute(self.read_subgraph_query_dict[hops], (seed_node_id,))
        results = self.session.fetchone()
        if results is None or results[-1] is None:
            return None, None
        
        feature_str, label_str, edge_str, node_ids_str = results
        
        features = np.array([row.split(',') for row in feature_str.split(';')], dtype=np.float32)
        labels = np.array([row.split(',') for row in label_str.split(';')], dtype=np.int32)
        subgraph_edges = np.array([row.split(',') for row in edge_str.split(';')], dtype=np.int32).transpose()
        node_ids = np.array(node_ids_str.split(','), dtype=np.int32)
        
        cols_source = np.searchsorted(node_ids, subgraph_edges[0])
        cols_target = np.searchsorted(node_ids, subgraph_edges[1])
        remapped_edge_index = np.vstack([cols_source, cols_target])
        
        read_time = time.time() - start
        return read_time, Subgraph(features=features, labels=labels, edge_index=remapped_edge_index, node_ids=node_ids)
    
    def update_nodes(self, node_id):
        """Updates a single node with pre-defined random data."""
        start = time.time()
        data_to_update = self.update_node_data + [node_id]
        self.session.execute(self.update_nodes_query, data_to_update)
        self.conn.commit()
        return time.time() - start
    
    def update_edges(self, selected_edge, new_target_id):
        """Updates a single edge, changing its target node."""
        start = time.time()
        source_id, target_id = selected_edge
        self.session.execute(self.update_edges_query, (new_target_id, int(source_id), int(target_id)))
        self.conn.commit()
        return time.time() - start
        
    def delete(self):
        """Deletes the entire database by removing the file."""
        start = time.time()
        self.close_session()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        return time.time() - start

    def close_session(self):
        """Closes the database connection."""
        if self.session:
            self.session.close()
            self.session = None
        if self.conn:
            self.conn.close()
            self.conn = None
