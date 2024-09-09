import pandas as pd
import torch
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv
import matplotlib.pyplot as plt

# Load and preprocess the data
def load_data(file_path):
    df = pd.read_csv("AAPL.csv")
    # Check if there are enough rows to train the model
    if len(df) < 2:
        raise ValueError("Not enough data to train the model.")
    
    # Select features (you might want to normalize or scale them)
    features = df[['Open', 'High', 'Low', 'Close', 'Volume']].values
    # Target: for simplicity, let's predict the closing price of the next day
    target = df['Close'].shift(-1).dropna().values
    features = features[:-1]  # Drop the last feature, as its target is NaN
    return features, target

# Prepare the graph
def create_graph(features):
    num_nodes = len(features)
    # Creating edges based on sequential time steps
    edges = []
    for i in range(num_nodes - 1):
        edges.append([i, i + 1])
    edges = torch.tensor(edges, dtype=torch.long).t().contiguous()
    return edges

# Define the GNN model
class GNN(torch.nn.Module):
    def __init__(self):
        super(GNN, self).__init__()
        self.conv1 = GCNConv(5, 16)  # Input features: 5, Output features: 16
        self.conv2 = GCNConv(16, 1)  # Output features: 1 (for prediction)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = x.relu()
        x = self.conv2(x, edge_index)
        return x

# Load data
features, target = load_data('AAPL.csv')
features = torch.tensor(features, dtype=torch.float)
target = torch.tensor(target, dtype=torch.float)

# Create graph
edges = create_graph(features)
data = Data(x=features, edge_index=edges)

# Initialize the model, loss function, and optimizer
model = GNN()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Train the model
def train(model, data, target, epochs=100):
    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        out = model(data)
        loss = criterion(out.squeeze(), target)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f'Epoch {epoch}: Loss = {loss.item()}')

train(model, data, target)

# Make predictions
model.eval()
with torch.no_grad():
    predictions = model(data).squeeze()

# Plot results
plt.figure(figsize=(12, 6))

# Create an array of indices to plot the data points
indices = range(len(target))

# Plot true prices
plt.plot(indices, target.numpy(), label='True Prices', color='blue', marker='o')

# Plot predicted prices
plt.plot(indices, predictions.numpy(), label='Predicted Prices', color='red', linestyle='--')

plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('AAPL Stock Price Prediction')
plt.legend()
plt.grid(True)
plt.show()
