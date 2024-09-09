import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

file_name = 'Intrusion detection\AAPL.csv'
data = pd.read_csv(file_name, index_col='date', parse_dates=True)
data['Price'] = data['Close']


model = IsolationForest(contamination=0.05)
data['anomaly'] = model.fit_predict(data[['Price']])
data['anomaly'] = data['anomaly'].map({1: 0, -1: 1})

# Plot the stock prices and mark the anomalies
# plt.figure(figsize=(10, 6))
# plt.plot(data.index, data['Price'], label='Price', color='blue')
# plt.scatter(data.index[data['anomaly'] == 1], 
#             data['Price'][data['anomaly'] == 1], 
#             color='red', 
#             label='Anomaly', 
#             marker='x', 
#             s=100)
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.title('Stock Price and Anomalies for AAPL')
# plt.legend()
# plt.show()


plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Price')
plt.scatter(data.index, data['Price'], color='red', label='Anomaly', marker='x', s=100)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price and Anomalies')
plt.legend()
plt.show()
