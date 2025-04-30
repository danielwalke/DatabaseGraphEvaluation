import torch
import random
import pandas as pd
import networkx as nx

"""
File to generate synthetic scale-free graph datasets with various input degrees 
"""
# We use a fixed seed for reproducibility.
RANDOM_SEED = 100000

for num_nodes in [1_000, 10_000, 100_000, 1_000_000]:
	print(num_nodes)
	# Create a directed scale-free graph.
	# The networkx.scale_free_graph returns a MultiDiGraph, which may have self-loops and parallel edges.
	G_multi = nx.scale_free_graph(num_nodes, seed=RANDOM_SEED)

	# Convert to a simple DiGraph (removes multiple edges).
	# Also remove self-loops.
	G = nx.DiGraph(G_multi)
	G.remove_edges_from(nx.selfloop_edges(G))

	# Retrieve the edges as a list of (source, target) tuples.
	edge_list = list(G.edges())

	# It’s a good idea to print some statistics about the graph
	in_degrees = dict(G.in_degree())
	out_degrees = dict(G.out_degree())
	print(f"Graph with {num_nodes} nodes:")
	print(f"  Number of edges: {G.number_of_edges()}")
	print(f"  In-degree stats: min={min(in_degrees.values())}, max={max(in_degrees.values())}")
	print(f"  Out-degree stats: min={min(out_degrees.values())}, max={max(out_degrees.values())}")

	# Create a PyTorch edge_index tensor.
	# edge_index should be a [2, num_edges] tensor.
	edge_index = torch.tensor(edge_list).t().type(torch.long)

	# -------------
	# Create node features and labels (similar to your original code)
	# -------------
	NUM_FEATURES = 100
	NUM_NODES = num_nodes
	node_idx = torch.arange(NUM_NODES)

	# For demonstration we generate random features.
	# (You could also include a scaling factor or other structure if desired.)
	X_rand_scaled = torch.rand(NUM_NODES, NUM_FEATURES)

	# Create node labels.
	# Here, the label is computed based on the sum of features.
	y_rand = X_rand_scaled.sum(dim=-1, keepdim=True)
	y = torch.round(y_rand / (NUM_FEATURES * NUM_NODES)).type(torch.int8)

	# -------------
	# Export to CSV files
	# -------------
	X_df = pd.DataFrame(X_rand_scaled.numpy())
	y_df = pd.DataFrame(y.numpy())
	# Transpose edge_index back to have rows represent individual edges.
	edge_index_df = pd.DataFrame(edge_index.t().numpy(), columns=["source", "target"])

	X_filename = f"X_{num_nodes}_nodes_scale_free.csv"
	y_filename = f"y_{num_nodes}_nodes_scale_free.csv"
	edge_index_filename = f"edge_index_{num_nodes}_nodes_scale_free.csv"

	X_df.to_csv(X_filename, index=False)
	y_df.to_csv(y_filename, index=False)
	edge_index_df.to_csv(edge_index_filename, index=False)

	print(f"Saved files: {X_filename}, {y_filename}, {edge_index_filename}")

	# -------------
	# (Optional) Read data back in to verify
	# -------------
	r_edge_index = pd.read_csv(edge_index_filename)
	print("Edge index tensor shape:", torch.from_numpy(r_edge_index.values).t().shape)

	r_y = pd.read_csv(y_filename)
	print("Labels shape:", torch.from_numpy(r_y.values).shape)

	r_X = pd.read_csv(X_filename)
	print("Node features shape:", torch.from_numpy(r_X.values).shape)
	print("-" * 50)
