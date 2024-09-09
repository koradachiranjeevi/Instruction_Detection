import torch
import torch.nn.functional as F
import pandas as pd
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv

# Load the dataset from a CSV file
df = pd.read_csv('aapl.csv')

# Node features (Prices)
x = torch.tensor(df['Price'].values.reshape(-1, 1), dtype=torch.float)

# Create edge connections (simple temporal edges)
# Connect each day to the next
edge_index = torch.tensor([list(range(len(df) - 1)), list(range(1, len(df)))], dtype=torch.long)

# Create the graph data object
data = Data(x=x, edge_index=edge_index)

# Define GCN model
class GCN(torch.nn.Module):
    def __init__(self):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(1, 16)
        self.conv2 = GCNConv(16, 1)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x

# Instantiate the model and run a forward pass
model = GCN()
output = model(data)

# Print the output
print(output)
