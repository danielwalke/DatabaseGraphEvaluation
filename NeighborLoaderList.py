from Data import Data
import numpy as np
from Subgraph import Subgraph
import time
import pandas as pd
import torch
from torch_geometric.utils import k_hop_subgraph, subgraph

class NeighborLoaderList():
    def __init__(self, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name, max_hops = 3):
        self.db_name = X_and_y_file_name.split(".")[0].lower()
        self.feature_file_name = feature_file_name
        self.label_file_name = label_file_name
        self.edge_file_name = edge_file_name
        self.session = None
        self.max_hops = max_hops
        self.edge_file_name = edge_file_name
        self.features = None
        self.labels = None
        self.edge_index = None

    @staticmethod
    def file_suffix():
        return "neighborloader_list"

    @staticmethod
    def db_name():
        return "neighborloader"

    def create(self):
        start = time.time()
        data = Data()
        data.read_and_initialize_data(self.feature_file_name, self.label_file_name, self.edge_file_name)
        self.features = torch.from_numpy(data.X.values).type(torch.float)
        self.labels = torch.from_numpy(data.y.values).type(torch.float)
        self.edge_index = torch.from_numpy(data.edge_index).type(torch.long)
        return time.time() - start
            
    def read(self, seed_node_id, hops):
        start = time.time()
        k_hop_nodes, _, _, _ = k_hop_subgraph(
            node_idx=seed_node_id,
            num_hops=hops,
            edge_index=self.edge_index,
            relabel_nodes=False,  # We want to keep original node IDs
            num_nodes=self.features.shape[0],
        )
        sorted_node_idx = torch.argsort(k_hop_nodes)
        k_hop_nodes = k_hop_nodes[sorted_node_idx]

        ## This includes edges in the subgraph that are not k hops away from my seed node
        final_edge_index, _ = subgraph(
            subset=k_hop_nodes,
            edge_index=self.edge_index,
            relabel_nodes=False, # Keep original node IDs
            num_nodes=self.features.shape[0]
        )
        final_edge_index = final_edge_index.numpy()
        cols_source = np.searchsorted(k_hop_nodes, final_edge_index[0])
        cols_target = np.searchsorted(k_hop_nodes, final_edge_index[1])
        remapped_final_edge_index = np.concatenate([np.expand_dims(cols_source, axis = 0), np.expand_dims(cols_target, axis = 0)], axis = 0)

        features = self.features[k_hop_nodes]
        labels = self.labels[k_hop_nodes]
        read_time = time.time() - start    
        return read_time, Subgraph(features = features.numpy(), labels = labels.numpy(), edge_index = remapped_final_edge_index, node_ids = k_hop_nodes.numpy())
    
    def update_nodes(self, node_id):
        start = time.time()
        update_time = time.time() - start
        return update_time
    
    def update_edges(self, selected_edge, new_target_id):
        start = time.time()
        return time.time() - start
        
    
    def delete(self):
        start = time.time()
        return time.time() - start

    def close_session(self):
        pass