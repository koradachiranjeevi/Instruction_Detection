import pandas as pd
from sklearn.ensemble import IsolationForest


file_name = 'AAPL.csv'
data = pd.read_csv(file_name, index_col='date', parse_dates=True)


data['Price'] = data['Close']


model = IsolationForest(contamination=0.05, random_state=42)
data['anomaly'] = model.fit_predict(data[['Price']])


data['anomaly'] = data['anomaly'].map({1: 0, -1: 1})


anomalies = data[data['anomaly'] == 1]

print("Anomalies detected at the following dates and times:")
for date in anomalies.index:
    print(date)
