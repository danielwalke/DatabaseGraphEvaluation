from ogb.nodeproppred import NodePropPredDataset
from torch_geometric.data import DataLoader

# Download and process data at './dataset/ogbg_molhiv/'
dataset = NodePropPredDataset(name = "ogbn-papers100M", root = 'ogbn_dataset/')
print(dataset.shape)
