from Data import Data
import numpy as np

class PostgresQuery(Data):
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        super().__init__()
        
        self.label_columns = []
        self.feature_columns = []
        self.create_db_query = None
        self.create_nodes_table_query = None
        self.create_edges_table_query = None
        self.create_nodes_query = None
        self.create_node_id_index_query = None
        self.create_edge_index_queries = []
        self.create_edges_query = None
        self.read_subgraph_query_dict = dict()
        self.update_nodes_query = None
        self.update_edges_query = None
        self.delete_query = None

    def intialize_columns(self):
        self.label_columns = list(filter(lambda col: "y" in col, self.X_and_y.columns))
        self.feature_columns = list(filter(lambda col: "f" in col, self.X_and_y.columns))

    def set_create_db_query(self):
        self.create_db_query = "CREATE DATABASE %s;"

    def set_create_nodes_table_query(self):
        column_types = ["id SERIAL PRIMARY KEY"]
        for col in self.X_and_y.columns:
            if "y" in col:
                column_types.append(f"{col} INTEGER")
                continue
            column_types.append(f"{col} REAL")
        self.create_nodes_table_query = f"""
        CREATE TABLE nodes (
            {",".join(column_types)}
        );
        """

    def set_create_edges_table_query(self):
        self.create_edges_table_query = """CREATE TABLE edges (
        source_id INTEGER NOT NULL,
        target_id INTEGER NOT NULL,
        FOREIGN KEY (source_id) REFERENCES nodes(id) ON DELETE CASCADE,
        FOREIGN KEY (target_id) REFERENCES nodes(id) ON DELETE CASCADE
    );
    """

    def set_create_nodes_query(self):
        self.create_nodes_query = "COPY nodes FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');"

    def set_create_node_id_index_query(self):
        self.create_node_id_index_query = "CREATE INDEX node_idx ON nodes (id);"

    def set_create_edge_indices_queries(self):
        self.create_edge_index_queries = ["CREATE INDEX source_idx ON edges (source_id);", "CREATE INDEX target_idx ON edges (target_id);", "CREATE INDEX source_target_idx ON edges (target_id, source_id);"]


    def set_create_edges_query(self):
        self.create_edges_query = "COPY edges (source_id, target_id) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');"
        
    def set_read_subgraph_query(self, hops):
        self.read_subgraph_query_dict[hops] = f"""
        WITH RECURSIVE NestedTargets AS (
            SELECT 0 AS depth, source_id, target_id
            FROM edges
            WHERE target_id = %s
            
            UNION ALL
            
            SELECT nt.depth + 1, e.source_id, e.target_id
            FROM edges e
            JOIN NestedTargets nt ON e.target_id = nt.source_id
            WHERE nt.depth < {hops - 1}
        ),
        
        node_ids AS (
            SELECT DISTINCT id FROM (
                SELECT source_id AS id FROM NestedTargets
                UNION
                SELECT target_id AS id FROM NestedTargets
            ) AS combined_ids
        ),
        
        node_data AS (
            SELECT 
                id, 
                {", ".join(self.X_and_y.columns)}
            FROM nodes
            WHERE id IN (SELECT id FROM node_ids)
            ORDER BY id
        )
        
        SELECT
            (SELECT array_agg(array[{", ".join(self.feature_columns)}]) FROM node_data) AS node_table,
            (SELECT array_agg(array[{", ".join(self.label_columns)}]) FROM node_data) AS label_table,
            (SELECT array_agg(array[source_id, target_id])
             FROM (SELECT DISTINCT source_id, target_id FROM NestedTargets) AS edges) AS edge_table,
             (SELECT array_agg(id) FROM node_data) AS node_ids;
    """

    def set_update_nodes_query(self):
        np.random.seed(42)
        features = np.random.rand(self.X.shape[-1]).tolist()
        labels = np.random.randint(0, 2, size=self.y.shape[-1]).tolist() 
        self.update_nodes_query = f"""
            UPDATE nodes 
            SET {",".join([f'{col} = {features[i]}' for i, col in enumerate(self.feature_columns)])}, {",".join([f'{col} = {int(labels[i])}' for i, col in enumerate(self.label_columns)])}
            WHERE id = %s;
            """
        
    def set_update_edges_query(self):
        self.update_edges_query = "UPDATE edges SET target_id = %s WHERE source_id = %s AND target_id = %s;"

    def set_delete_query(self):
        self.delete_query = "DROP DATABASE IF EXISTS %s;"
        
    def initialize_all_queries_columns(self, max_hops):
        self.intialize_columns()
        self.set_create_db_query()
        self.set_create_nodes_table_query()
        self.set_create_edges_table_query()
        self.set_create_nodes_query()
        self.set_create_node_id_index_query()
        self.set_create_edge_indices_queries()
        self.set_create_edges_query()
        for hops in range(1, max_hops + 1):
            self.set_read_subgraph_query(hops)
        self.set_update_nodes_query()
        self.set_update_edges_query()
        self.set_delete_query()