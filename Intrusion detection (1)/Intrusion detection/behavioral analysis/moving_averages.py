import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('AAPL.csv', index_col='date', parse_dates=True)

# Moving Averages
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Plotting Price and Moving Averages
plt.figure(figsize=(14, 6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA_20'], label='20-Day SMA', linestyle='--')
plt.plot(data['SMA_50'], label='50-Day SMA', linestyle='--')
plt.title('Stock Price and Moving Averages')
plt.legend()
plt.show()
