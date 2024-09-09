import os
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Function to fetch stock data from Alpha Vantage
def fetch_stock_data(symbol, api_key):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    
    # Rename columns for easier reference
    data.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    }, inplace=True)
    
    return data

# Function to save stock data to a CSV file
def save_stock_data_to_csv(symbol, data):
    filename = os.path.join('.', f"{symbol.upper()}.csv")
    data.to_csv(filename)
    print(f"Data for {symbol.upper()} saved to {filename}")

# Function to analyze stock data
def analyze_stock_data(data):
    # Moving Averages
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    # Volatility (Standard Deviation)
    data['Returns'] = data['Close'].pct_change()
    volatility = data['Returns'].std()
    
    # Bollinger Bands
    data['20d_MA'] = data['Close'].rolling(window=20).mean()
    data['20d_std'] = data['Close'].rolling(window=20).std()
    data['Upper_Band'] = data['20d_MA'] + (data['20d_std'] * 2)
    data['Lower_Band'] = data['20d_MA'] - (data['20d_std'] * 2)
    
    # RSI
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD
    data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    # Volume Trend
    data['Volume_MA'] = data['Volume'].rolling(window=20).mean()
    
    # Plotting
    plt.figure(figsize=(14, 16))
    
    # Price and Moving Averages
    plt.subplot(4, 1, 1)
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA_20'], label='20-Day SMA', linestyle='--')
    plt.plot(data['SMA_50'], label='50-Day SMA', linestyle='--')
    plt.title('Stock Price and Moving Averages')
    plt.legend()
    
    # Bollinger Bands
    plt.subplot(4, 1, 2)
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['20d_MA'], label='20-Day MA', linestyle='--')
    plt.plot(data['Upper_Band'], label='Upper Band', linestyle='--')
    plt.plot(data['Lower_Band'], label='Lower Band', linestyle='--')
    plt.title('Bollinger Bands')
    plt.legend()
    
    # RSI
    plt.subplot(4, 1, 3)
    plt.plot(data['RSI'], label='RSI', color='orange')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()
    
    # Volume
    plt.subplot(4, 1, 4)
    plt.plot(data['Volume'], label='Volume')
    plt.plot(data['Volume_MA'], label='Volume MA', linestyle='--')
    plt.title('Volume and Moving Average')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Main execution
api_key = 'T6IF9M2WT9TU9NGL'  # Replace with your own Alpha Vantage API key
symbol = 'AAPL'  # Replace with the stock symbol you want to analyze

# Fetch and save stock data
data = fetch_stock_data(symbol, api_key)
save_stock_data_to_csv(symbol, data)

# Analyze and plot stock data
analyze_stock_data(data)
