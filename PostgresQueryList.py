from PostgresQuery import PostgresQuery
import numpy as np

class PostgresQueryList(PostgresQuery):
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        super().__init__(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        
    def set_create_nodes_table_query(self):
        column_types = ["id SERIAL PRIMARY KEY"]
        for col in self.X_and_y.columns:
            if col == "y":
                column_types.append(f"{col} INTEGER[]")
                continue
            column_types.append(f"{col} REAL[]")
        
        self.create_nodes_table_query = f"""
        CREATE TABLE nodes (
            {",".join(column_types)}
        );
        """
        
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
            (SELECT array_agg({", ".join(self.X_and_y.columns[:-1])}) FROM node_data) AS node_table,
            (SELECT array_agg({self.X_and_y.columns[-1]}) FROM node_data) AS label_table,
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
            SET X = ARRAY{features}, y = ARRAY{labels}
            WHERE id = %s;
        """
        
    def initialize_all_queries_columns(self, max_hops):
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