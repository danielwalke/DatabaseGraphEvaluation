from Data import Data
import numpy as np

class SQLiteQuery(Data):
    """
    Defines the SQL query strings for SQLite operations with a columnar schema.
    This class prepares all necessary SQL statements for creating tables,
    importing data, reading subgraphs, and performing updates and deletions.
    """
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        super().__init__()
        
        # Initialize properties to hold query strings
        self.label_columns = []
        self.feature_columns = []
        self.create_nodes_table_query = None
        self.create_edges_table_query = None
        self.create_node_id_index_query = None
        self.create_edge_index_queries = []
        self.read_subgraph_query_dict = dict()
        self.update_nodes_query = None
        self.update_edges_query = None
        # In SQLite, deletion is handled by removing the file.

    def intialize_columns(self):
        """Identifies feature and label columns from the dataframe."""
        self.label_columns = list(filter(lambda col: "y" in col, self.X_and_y.columns))
        self.feature_columns = list(filter(lambda col: "f" in col, self.X_and_y.columns))

    def set_create_nodes_table_query(self):
        """Sets the query to create the 'nodes' table with a columnar schema."""
        column_types = ["id INTEGER PRIMARY KEY"]
        # Define column types based on their names
        for col in self.X_and_y.columns:
            if "y" in col:
                column_types.append(f"{col} INTEGER")
            else:
                column_types.append(f"{col} REAL")
        
        self.create_nodes_table_query = f"""
        CREATE TABLE IF NOT EXISTS nodes (
            {", ".join(column_types)}
        );
        """

    def set_create_edges_table_query(self):
        """Sets the query to create the 'edges' table."""
        self.create_edges_table_query = """
        CREATE TABLE IF NOT EXISTS edges (
            source_id INTEGER NOT NULL,
            target_id INTEGER NOT NULL,
            FOREIGN KEY (source_id) REFERENCES nodes(id) ON DELETE CASCADE,
            FOREIGN KEY (target_id) REFERENCES nodes(id) ON DELETE CASCADE
        );
        """

    def set_create_node_id_index_query(self):
        """Sets the query to create an index on the 'id' column of the 'nodes' table."""
        self.create_node_id_index_query = "CREATE INDEX IF NOT EXISTS node_idx ON nodes (id);"

    def set_create_edge_indices_queries(self):
        """Sets queries to create indices on the 'edges' table for faster lookups."""
        self.create_edge_index_queries = [
            "CREATE INDEX IF NOT EXISTS source_idx ON edges (source_id);",
            "CREATE INDEX IF NOT EXISTS target_idx ON edges (target_id);",
            "CREATE INDEX IF NOT EXISTS source_target_idx ON edges (target_id, source_id);"
        ]
        
    def set_read_subgraph_query(self, hops):
        """
        Sets the recursive query to read a k-hop subgraph.
        It uses GROUP_CONCAT to aggregate data into strings, which are parsed in Python.
        """
        # Concatenators for feature and label columns
        feature_concat = " || ',' || ".join(self.feature_columns)
        label_concat = " || ',' || ".join(self.label_columns)

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
            (SELECT GROUP_CONCAT(features, ';') FROM (SELECT {feature_concat} AS features FROM node_data)) AS feature_table,
            (SELECT GROUP_CONCAT(labels, ';') FROM (SELECT {label_concat} AS labels FROM node_data)) AS label_table,
            (SELECT GROUP_CONCAT(source_id || ',' || target_id, ';') FROM (SELECT DISTINCT source_id, target_id FROM NestedTargets)) AS edge_table,
            (SELECT GROUP_CONCAT(id, ',') FROM node_data) AS node_ids;
        """

    def set_update_nodes_query(self):
        """Sets the query to update a node's features and labels."""
        np.random.seed(42)
        # Generate placeholder values for the update
        features = np.random.rand(len(self.feature_columns)).tolist()
        labels = np.random.randint(0, 2, size=len(self.label_columns)).tolist()
        
        set_clauses = [f"{col} = ?" for col in self.feature_columns] + [f"{col} = ?" for col in self.label_columns]
        
        self.update_nodes_query = f"""
            UPDATE nodes 
            SET {", ".join(set_clauses)}
            WHERE id = ?;
            """
        # Store the randomly generated data to be used when executing the query
        self.update_node_data = features + labels

    def set_update_edges_query(self):
        """Sets the query to update an edge's target node."""
        self.update_edges_query = "UPDATE edges SET target_id = ? WHERE source_id = ? AND target_id = ?;"
        
    def initialize_all_queries(self, max_hops):
        """Initializes all query strings."""
        self.intialize_columns()
        self.set_create_nodes_table_query()
        self.set_create_edges_table_query()
        self.set_create_node_id_index_query()
        self.set_create_edge_indices_queries()
        for hops in range(1, max_hops + 1):
            self.set_read_subgraph_query(hops)
        self.set_update_nodes_query()
        self.set_update_edges_query()

