from flask import Flask, jsonify, render_template
import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

app = Flask(__name__)

def fetch_stock_data(symbol, api_key):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='compact')
    data.rename(columns={
        '1. open': 'Open', 
        '2. high': 'High', 
        '3. low': 'Low', 
        '4. close': 'Close', 
        '5. volume': 'Volume'}, inplace=True)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stock_data/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    api_key = 'T6IF9M2WT9TU9NGL'
    data = fetch_stock_data(symbol, api_key)
    data = data.tail(10)  # Get the last 10 entries for simplicity
    return jsonify(data.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
