from Neo4jQuery import Neo4jQuery
import numpy as np

class Neo4jQueryList(Neo4jQuery):
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        super().__init__(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        self.create_nodes_query = None
        self.create_node_id_index_query = None
        self.create_edges_query = None
        self.read_subgraph_query_dict = dict()
        self.update_nodes_query = None
        self.update_edges_query = None
        self.delete_query = None

    def set_create_nodes_columns_query(self):
        # self.create_nodes_query = """
        #         LOAD CSV WITH HEADERS FROM $file AS line
        #         WITH line, linenumber() AS index
        #         CALL (line, index) {
        #           MERGE (p:Node {id: index - 2})
        #           SET p.label = apoc.convert.fromJsonList(line["y"])
        #           SET p.features = apoc.convert.fromJsonList(line["X"])
        #         } IN TRANSACTIONS OF 1000 ROWS
        #         """
        self.create_nodes_query = """
                LOAD CSV WITH HEADERS FROM $file AS line
                WITH line, linenumber() AS index,
                     split(trim(replace(replace(line.y, '[', ''), ']', '')), ',') AS labelList,
                     split(trim(replace(replace(line.X, '[', ''), ']', '')), ',') AS featureList
                MERGE (p:Node {id: index - 2})
                SET p.label = [x IN labelList | toFloat(trim(x))],
                    p.features = [x IN featureList | toFloat(trim(x))]
                """
        
    def set_read_subgraph_columns_query(self, hops):
        # self.read_subgraph_query_dict[hops] = f"""
        #     MATCH (t {{id: $seed_node_id}})
        #         MATCH (s)-[r*0..{hops}]->(t)
        #         UNWIND r AS edge
        #         WITH t, edge
        #         WITH 
        #           collect(DISTINCT [startNode(edge).id, endNode(edge).id]) AS edges,
        #           collect(DISTINCT startNode(edge)) AS startNodes,
        #           t AS endNode
        #         UNWIND (startNodes + [endNode]) AS node
        #         WITH edges, COLLECT(DISTINCT node) AS uniqueNodes
        #         UNWIND uniqueNodes AS node
        #         WITH edges, node, node.features AS nodeFeatures
        #         ORDER BY node.id
        #         RETURN 
        #           edges,
        #           collect(node.id) AS idCollection,
        #           collect(node.label) AS labels,
        #           collect(nodeFeatures) AS features
        # """
        self.read_subgraph_query_dict[hops] = f"""
        MATCH path = (:Node {{id: $seed_node_id}}) ((:Node)<-[:connects]-(:Node)){{1,{hops}}}
        (:Node )
        WITH COLLECT(nodes(path)) AS allNodesPaths, COLLECT(apoc.coll.pairsMin(nodes(path))) AS allEdgesPairs  
        WITH apoc.coll.toSet(apoc.coll.flatten(allNodesPaths)) AS uniqueNodes, 
        apoc.coll.toSet(apoc.coll.flatten(allEdgesPairs)) AS uniqueEdges 
        RETURN 
                [e IN uniqueEdges | [e[1].id, e[0].id]] AS edges,
                [node IN uniqueNodes | node.id] AS idCollection, 
                [node IN uniqueNodes | node.label] AS labels, 
                [node IN uniqueNodes | node.features] AS features;
        """

    def set_update_nodes_query(self):
        np.random.seed(42)
        features = np.random.rand(self.X.shape[-1]).tolist()
        labels = np.random.randint(0, 2, size=self.y.shape[-1]).tolist()  
        self.update_nodes_query = f"""
        MATCH (n:Node {{id: $node_id}})
        SET n.features = {features}
        SET n.label = {labels}
        """
        
    def initialize_all_queries_columns(self, max_hops):
        self.set_create_nodes_columns_query()
        self.set_create_node_id_index_query()
        self.set_create_edges_query()
        for hops in range(1, max_hops + 1):
            self.set_read_subgraph_columns_query(hops)
        self.set_update_nodes_query()
        self.set_update_edges_query()
        self.set_delete_query()