import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def fetch_stock_data(symbol, api_key):
    
    ts = TimeSeries(key=api_key, output_format='pandas')
    
 
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    
    
    data.rename(columns={
        '1. open': 'Open', 
        '2. high': 'High', 
        '3. low': 'Low', 
        '4. close': 'Close', 
        '5. volume': 'Volume'}, inplace=True)
    
    return data

def save_stock_data_to_csv(symbol, data):
   
    filename = f"{symbol.upper()}.csv"
    
   
    data.to_csv(filename)
    
    print(f"Data for {symbol.upper()} saved to {filename}")


api_key = 'T6IF9M2WT9TU9NGL'


symbol = 'AAPL'


data = fetch_stock_data(symbol, api_key)


save_stock_data_to_csv(symbol, data)


