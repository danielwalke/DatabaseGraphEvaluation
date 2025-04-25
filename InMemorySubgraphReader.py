from Data import Data
from Subgraph import Subgraph
import numpy as np

class InMemSubGraphReader(Data):
    
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        super().__init__()
        self.intialize_column_data(feature_file_name, label_file_name, edge_file_name, f"in_mem_{X_and_y_file_name}")
        pass

    def recurse_edge_index_iterative(self, source_nodes, max_depth):
        visited_nodes = set(source_nodes)
        current_frontier = np.array(source_nodes)
        
        subgraph_edges = []
    
        for _ in range(max_depth):
            target_mask = np.isin(self.edge_index[1], current_frontier)
            subgraph_edge_index = self.edge_index[:, target_mask]
            subgraph_edges.append(subgraph_edge_index)
    
            current_frontier = np.setdiff1d(subgraph_edge_index[0], list(visited_nodes))
            visited_nodes.update(current_frontier)
            
            if len(current_frontier) == 0:
                break
    
        return np.concatenate(subgraph_edges, axis=1) if subgraph_edges else np.empty((2, 0), dtype=self.edge_index.dtype)

    def get_subgraph_from_in_mem_graph(self, seed_node_id, hops):
        subgraph_edge_index = self.recurse_edge_index_iterative([seed_node_id], hops)
        
        unique_node_ids, remapping = np.unique(subgraph_edge_index, return_inverse=True)
        
        features = self.X.iloc[unique_node_ids, :].values
        labels = self.y.iloc[unique_node_ids, :].values.squeeze()
    
        remapped_edge_index = remapping.reshape(2, -1)
        return Subgraph(features = features, labels = labels, edge_index = remapped_edge_index, node_ids = unique_node_ids)