import numpy as np
import time
import torch
from torch_geometric.utils import sort_edge_index
import gc
from InMemorySubgraphReader import InMemSubGraphReader
from tqdm import tqdm

class CRUD_Evaluator(InMemSubGraphReader):
    def __init__(self, Dbms_evaluator_class, feature_file_name, label_file_name, edge_file_name, X_and_y_file_name):
        self.dbms_evaluator = Dbms_evaluator_class(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        super().__init__(feature_file_name, label_file_name, edge_file_name, X_and_y_file_name)
        pass

    def create(self):
        print("Create")
        return self.dbms_evaluator.create()

    def read(self, hops, assert_ids = True,assert_edge_index = True, assert_features = True, assert_labels = True, random_sample_size = 1_000):
        print("Read")
        np.random.seed(42)
        seed_node_ids = np.random.choice(np.arange(self.X_and_y.shape[0]), size = random_sample_size, replace = False)
        complete_query_time = 0
        complete_test_time = 0
        for seed_node_id in tqdm(seed_node_ids, desc=f"Reading subgraphs of order {str(hops)}"):
            query_time, subgraph = self.dbms_evaluator.read(seed_node_id, hops)
            if subgraph is None: continue
            complete_query_time += query_time
            
            start = time.time()
            test_subgraph = self.get_subgraph_from_in_mem_graph(seed_node_id, hops)        
            complete_test_time += time.time() - start         

            if assert_ids:
                assert np.allclose(subgraph.node_ids, test_subgraph.node_ids), "Node ids does not match"
                del test_subgraph.node_ids
                del subgraph.node_ids
                gc.collect()
            if assert_edge_index:
                assert (sort_edge_index(torch.from_numpy(test_subgraph.edge_index)) == sort_edge_index(torch.from_numpy(subgraph.edge_index))).sum() / (test_subgraph.edge_index.shape[-1] * test_subgraph.edge_index.shape[0]), "Edges does not match"
                del test_subgraph.edge_index
                del subgraph.edge_index
                gc.collect()
            if assert_features:
                assert np.allclose(subgraph.features.astype(np.float32), test_subgraph.features.astype(np.float32)), "Features does not match"
                del test_subgraph.features
                del subgraph.features
                gc.collect()
            if assert_labels:
                assert np.allclose(subgraph.labels.astype(np.int8), test_subgraph.labels.astype(np.int8)), "Labels does not match"
                ## Could unsqueeze labels solve the malloc problem?
                del test_subgraph.labels
                del subgraph.labels
                gc.collect()
        return complete_query_time, complete_test_time
            
            

    def update_nodes(self, random_sample_size = 1_000):
        print("Update nodes")
        np.random.seed(42)
        node_ids = np.random.choice(np.arange(self.X_and_y.shape[0]), size = random_sample_size, replace = False).tolist()
        overall_update_time = 0
        for node_id in tqdm(node_ids, desc="Updating nodes"):
            update_time = self.dbms_evaluator.update_nodes(node_id)
            overall_update_time += update_time
        return overall_update_time

    def update_edges(self, random_sample_size = 1_000):
        print("Update edges")
        np.random.seed(42)
        edge_ids = np.random.choice(np.arange(self.edge_index.shape[-1]),
                                    size=random_sample_size,
                                    replace=False).tolist()
        selected_edges = self.edge_index[:, edge_ids].transpose(-1, 0)
        overall_update_time = 0
        for selected_edge in tqdm(selected_edges, desc="Updating edges"):
            source_id, target_id = selected_edge
            np.random.seed(42)
            new_target_id = int(np.random.randint(0, self.X_and_y.shape[0]))
            update_time = self.dbms_evaluator.update_edges(selected_edge, new_target_id)
            overall_update_time += update_time
        return overall_update_time

    def update(self):
        print("Update")
        node_update_time = self.update_nodes()
        edge_update_time = self.update_edges()
        return node_update_time + edge_update_time

    def delete(self):
        print("Delete")
        delete_time = self.dbms_evaluator.delete()
        return delete_time
        

