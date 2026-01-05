from SQLiteQuery import SQLiteQuery
import numpy as np
import json

class SQLiteQueryList(SQLiteQuery):
    """
    Defines SQLite queries for a schema where features and labels are
    stored as serialized JSON strings in JSON columns.
    """
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        super().__init__(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        
    def set_create_nodes_table_query(self):
        """
        Overrides the base method to create a 'nodes' table
        where 'X' (features) and 'y' (labels) are stored in JSON columns.
        """
        self.create_nodes_table_query = """
        CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY,
            X JSON,
            y JSON
        );
        """
        
    def set_read_subgraph_query(self, hops):
        """
        Overrides the base method to read from the JSON-based schema.
        It uses json_group_array to aggregate data efficiently.
        """
        self.read_subgraph_query_dict[hops] = f"""
        WITH RECURSIVE NestedTargets AS (
            SELECT 0 AS depth, source_id, target_id
            FROM edges
            WHERE target_id = ?
            
            UNION ALL
            
            SELECT nt.depth + 1, e.source_id, e.target_id
            FROM edges e
            JOIN NestedTargets nt ON e.target_id = nt.source_id
            WHERE nt.depth < {hops - 1}
        ),
        
        node_ids_cte AS (
            SELECT DISTINCT id FROM (
                SELECT source_id AS id FROM NestedTargets
                UNION
                SELECT target_id AS id FROM NestedTargets
            )
        ),

        node_data AS (
            SELECT * FROM nodes
            WHERE id IN (SELECT id FROM node_ids_cte)
            ORDER BY id
        )

        SELECT
            (SELECT json_group_array(X) FROM node_data) AS feature_table,
            (SELECT json_group_array(y) FROM node_data) AS label_table,
            (SELECT GROUP_CONCAT(source_id || ',' || target_id, ';') FROM (SELECT DISTINCT source_id, target_id FROM NestedTargets)) AS edge_table,
            (SELECT GROUP_CONCAT(id, ',') FROM node_data) AS node_ids;
        """

    def set_update_nodes_query(self):
        """
        Overrides the base method to update a node with serialized JSON data.
        """
        np.random.seed(42)
        # Generate new data and serialize it as a JSON string
        features = np.random.rand(self.X.shape[-1]).tolist()
        labels = np.random.randint(0, 2, size=self.y.shape[-1]).tolist()
        
        features_json = json.dumps(features)
        labels_json = json.dumps(labels)

        self.update_nodes_query = """
            UPDATE nodes 
            SET X = ?, y = ?
            WHERE id = ?;
        """
        # Store the serialized data for execution
        self.update_node_data = (features_json, labels_json)
        
    def initialize_all_queries(self, max_hops):
        """Initializes all queries for the JSON-based schema."""
        self.set_create_nodes_table_query()
        self.set_create_edges_table_query()
        self.set_create_node_id_index_query()
        self.set_create_edge_indices_queries()
        for hops in range(1, max_hops + 1):
            self.set_read_subgraph_query(hops)
        self.set_update_nodes_query()
        self.set_update_edges_query()
