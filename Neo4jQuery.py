from Data import Data
import numpy as np

class Neo4jQuery(Data):
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        super().__init__()
        self.create_nodes_query = None
        self.create_node_id_index_query = None
        self.create_edges_query = None
        self.read_subgraph_query_dict = dict()
        self.update_nodes_query = None
        self.update_edges_query = None
        self.delete_query = None

    def intialize_columns_getters_and_setters(self):
        self.label_columns = list(filter(lambda col: "y" in col, self.X_and_y.columns))
        self.feature_columns = list(filter(lambda col: "f" in col, self.X_and_y.columns))
        self.label_columns_setter = "\n".join([f"SET p['{col}'] = toInteger(line['{col}'])" for col in self.label_columns])
        self.feature_columns_setter = "\n".join([f"SET p['{col}'] = toFloat(line['{col}'])" for col in self.feature_columns])
        feature_columns_getter = ",".join([f"node['{col}']" for col in self.feature_columns])
        self.feature_columns_getter = f'[{feature_columns_getter}] as nodeFeatures'
        label_columns_getter = ",".join([f"node['{col}']" for col in self.label_columns])
        self.label_columns_getter = f'[{label_columns_getter}] as nodeLabels'

    def set_create_nodes_columns_query(self):
        self.create_nodes_query = f"""
                    LOAD CSV WITH HEADERS FROM $file AS line
                    WITH line, linenumber() AS index
                    CALL (line, index) {{
                      MERGE (p:Node {{id: index - 2}})
                      {self.label_columns_setter}
                      {self.feature_columns_setter}
                    }} IN TRANSACTIONS OF 10000 ROWS
                    """

    def set_create_node_id_index_query(self):
        self.create_node_id_index_query = "CREATE INDEX IF NOT EXISTS FOR (n:Node) ON (n.id)"

    def set_create_edges_query(self):
        self.create_edges_query = """
                LOAD CSV FROM $file AS line
                WITH line, linenumber() AS index
                WHERE index <> 1
                CALL (line) {
                    MATCH (s:Node {id: toInteger(line[0])}), (t:Node {id: toInteger(line[1])})
                    CREATE (s)-[r:connects]->(t)
                } IN TRANSACTIONS OF 10000 ROWS
                """
        
    def set_read_subgraph_columns_query(self, hops):
        self.read_subgraph_query_dict[hops] = f"""
            MATCH (t {{id: $seed_node_id}})
            MATCH (s)-[r*0..{hops}]->(t)
            UNWIND r AS edge
            WITH t, edge
            WITH 
              collect(DISTINCT [startNode(edge).id, endNode(edge).id]) AS edges,
              collect(DISTINCT startNode(edge)) AS startNodes,
              t AS endNode
            UNWIND (startNodes + [endNode]) AS node
            WITH edges, COLLECT(DISTINCT node) AS uniqueNodes
            UNWIND uniqueNodes AS node
            WITH edges, node.id as nodeId, {self.feature_columns_getter}, {self.label_columns_getter}
            ORDER BY nodeId
            RETURN 
              edges,
              collect(nodeId) AS idCollection,
              collect(nodeLabels) AS labels,
              collect(nodeFeatures) AS features
        """
        ## ORDER BY nodeId seems to increase speed 

    def set_update_nodes_query(self):
        np.random.seed(42)
        features = np.random.rand(self.X.shape[-1]).tolist()
        labels = np.random.randint(0, 2, size=self.y.shape[-1]).tolist() 
        label_columns_setter = "\n".join([f"SET n['{col}'] = {int(labels[i])}" for i, col in enumerate(self.label_columns)])
        feature_columns_setter = "\n".join([f"SET n['{col}'] = {features[i]}" for i, col in enumerate(self.feature_columns)])
        self.update_nodes_query = f"""
        MATCH (n:Node {{id: $node_id}})
        {label_columns_setter}
        {feature_columns_setter}
        """
        
    def set_update_edges_query(self):
        self.update_edges_query = """
                MATCH (s {id: $source_id}), (t {id: $target_id}), (new_t {id: $new_target_id})
                MATCH (s)-[r:connects]->(t)
                DELETE r
                CREATE (s)-[new_r:connects]->(new_t)
                """

    def set_delete_query(self):
        self.delete_query = "MATCH (n) DETACH DELETE(n)"
        
    def initialize_all_queries_columns(self, max_hops):
        self.intialize_columns_getters_and_setters()
        self.set_create_nodes_columns_query()
        self.set_create_node_id_index_query()
        self.set_create_edges_query()
        for hops in range(1, max_hops + 1):
            self.set_read_subgraph_columns_query(hops)
        self.set_update_nodes_query()
        self.set_update_edges_query()
        self.set_delete_query()