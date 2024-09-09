import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np


file_name = 'AAPL.csv'
data = pd.read_csv(file_name, index_col='date', parse_dates=True)


data['Price'] = data['Close']
data['Volume'] = data['Volume']


data['Returns'] = data['Price'].pct_change()


data = data.dropna()


features = data[['Price', 'Volume', 'Returns']]


model = IsolationForest(contamination=0.05, random_state=42, n_estimators=100)
data['anomaly'] = model.fit_predict(features)


data['anomaly'] = data['anomaly'].map({1: 0, -1: 1})

anomalies = data[data['anomaly'] == 1]

print("Potential Market Manipulation detected at the following dates and times:")
for date, row in anomalies.iterrows():
    print(f"Date: {date}, Price: {row['Price']}, Volume: {row['Volume']}, Returns: {row['Returns']}")


anomalies.to_csv('AAPL_anomalies.csv')


# Large Returns: Significant percentage changes (either positive or negative) can be indicative of manipulation attempts, especially if they occur alongside large changes in trading volume.
# Patterns: Repeated patterns of large returns may suggest manipulation strategies such as pump-and-dump schemes or other forms of market manipulation.