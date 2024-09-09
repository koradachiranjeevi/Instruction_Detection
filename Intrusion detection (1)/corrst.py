import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# List of medical sector stock tickers
tickers = ['JNJ', 'PFE', 'ABT', 'MRK', 'LLY']

# Download historical data for these stocks
data = yf.download(tickers, start="2020-01-01", end="2023-01-01")['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change()

# Compute the correlation matrix
correlation_matrix = daily_returns.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Medical Sector Stocks')
plt.show()
