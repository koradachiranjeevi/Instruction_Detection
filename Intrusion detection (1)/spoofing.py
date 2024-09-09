import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
initial_price = 150  # Starting price of AAPL stock (in USD)
num_trades = 100  # Number of trades to simulate
price = initial_price
prices = [price]  # To store the price history

# Simulate buy/sell transactions
np.random.seed(42)  # For reproducibility

def execute_trade(action, volume, price):
    """Adjusts the stock price based on the action (buy or sell) and volume."""
    price_change = volume * 0.01  # Simulate the impact of volume on price
    if action == "buy":
        return price + price_change  # Price increases on buy
    elif action == "sell":
        return price - price_change  # Price decreases on sell

# Simulate normal market conditions
for i in range(num_trades):
    # Randomly decide whether it's a buy or sell order
    action = np.random.choice(["buy", "sell"], p=[0.5, 0.5])
    volume = np.random.randint(1, 20)  # Simulate varying trade volumes (1 to 20 units)
    
    price = execute_trade(action, volume, price)
    prices.append(price)

# Simulate massive sell-off
massive_sell_volume = 200  # Huge sell order
price = execute_trade("sell", massive_sell_volume, price)
prices.append(price)

# Simulate massive buy-in
massive_buy_volume = 200  # Huge buy order
price = execute_trade("buy", massive_buy_volume, price)
prices.append(price)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(prices, label='Stock Price')
plt.axvline(x=num_trades, color='r', linestyle='--', label='Massive Sell')
plt.axvline(x=num_trades + 1, color='g', linestyle='--', label='Massive Buy')
plt.title('Stock Price Simulation with Massive Buy and Sell')
plt.xlabel('Number of Trades')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.show()
