import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('AAPL.csv', index_col='date', parse_dates=True)

# Bollinger Bands
data['20d_MA'] = data['Close'].rolling(window=20).mean()
data['20d_std'] = data['Close'].rolling(window=20).std()
data['Upper_Band'] = data['20d_MA'] + (data['20d_std'] * 2)
data['Lower_Band'] = data['20d_MA'] - (data['20d_std'] * 2)

# Plotting Bollinger Bands
plt.figure(figsize=(14, 6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['20d_MA'], label='20-Day MA', linestyle='--')
plt.plot(data['Upper_Band'], label='Upper Band', linestyle='--')
plt.plot(data['Lower_Band'], label='Lower Band', linestyle='--')
plt.title('Bollinger Bands')
plt.legend()
plt.show()
