import torch
import random
import pandas as pd

"""
File to generate synthetic datasets with fixed number of input edges
"""
for num_nodes in [1_000_000]: #1_000,10_000, 100_000
    for num_edges in [5]: #5,10,20
        ## Configs
        NUM_FEATURES = 100
        NUM_NODES = num_nodes
        IN_EDGES_PER_NODE = num_edges

        ## Features for nodes scaled based on index (nodes with higher indexes have larger feature values for each dimension)
        node_idx = torch.arange(NUM_NODES)
        # X_rand = torch.ones(NUM_NODES, NUM_FEATURES)
        # X_rand_scaled = node_idx.unsqueeze(0).repeat(NUM_FEATURES, 1).t() * X_rand

        ## add some noise to features
        X_rand_scaled = torch.rand(NUM_NODES, NUM_FEATURES) # torch.rand_like(X_rand_scaled) + X_rand_scaled

        ##Node labels based on summed and rounded feature values
        y_rand = X_rand_scaled.sum(-1).unsqueeze(-1)
        y = torch.round(y_rand / (NUM_FEATURES * NUM_NODES)).type(torch.int8)

        ## Edge index with pre-defined in-degree, i.e., every node has the number of incoming nodes
        edge_set = set()
        source_node_list = node_idx.tolist()
        target_node_list = node_idx.tolist()
        target_deg = {node: 0 for node in target_node_list}

        random.seed(100000)
        while IN_EDGES_PER_NODE * NUM_NODES != len(edge_set):
            source_node = random.choice(source_node_list)
            target_node = random.choice(target_node_list)
            pair = (source_node, target_node)
            if pair in edge_set:
                continue
            target_deg[target_node] += 1
            if target_deg[target_node] == IN_EDGES_PER_NODE:
                target_node_list.remove(target_node)
            edge_set.add(pair)
            if len(edge_set) % 1000 == 0:
                print(len(edge_set))

        edge_index = torch.tensor(list(edge_set)).t().type(torch.long)

        ## to dataframe for csv export
        X = pd.DataFrame(X_rand_scaled.numpy())
        y = pd.DataFrame(y.numpy())
        edge_index = pd.DataFrame(edge_index.t().numpy())
        edge_index.to_csv(f"edge_index_{str(NUM_NODES)}_nodes_{str(IN_EDGES_PER_NODE)}_edges.csv", index=False)
        y.to_csv(f"y_{str(NUM_NODES)}_nodes_{str(IN_EDGES_PER_NODE)}_edges.csv", index=False)
        X.to_csv(f"X_{str(NUM_NODES)}_nodes_{str(IN_EDGES_PER_NODE)}_edges.csv", index=False)

        ## reading data in
        r_edge_index = pd.read_csv(f"edge_index_{str(NUM_NODES)}_nodes_{str(IN_EDGES_PER_NODE)}_edges.csv")
        print(torch.from_numpy(r_edge_index.values).t())
        r_y = pd.read_csv(f"y_{str(NUM_NODES)}_nodes_{str(IN_EDGES_PER_NODE)}_edges.csv")
        print(torch.from_numpy(r_y.values).shape)
        r_X = pd.read_csv(f"X_{str(NUM_NODES)}_nodes_{str(IN_EDGES_PER_NODE)}_edges.csv")
        print(torch.from_numpy(r_X.values).shape)

