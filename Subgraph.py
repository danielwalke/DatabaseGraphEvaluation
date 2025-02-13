class Subgraph:
    def __init__(self, features, labels, edge_index, node_ids):
        self.features = features
        self.labels = labels
        self.edge_index = edge_index
        self.node_ids = node_ids
    