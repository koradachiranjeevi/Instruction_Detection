import csv
import shutil
import pandas as pd

# Step 1: Create the Original CSV File
stock_data = [
    {"Date": "2024-08-01", "Stock": "AAPL", "Price": 150.25},
    {"Date": "2024-08-02", "Stock": "AAPL", "Price": 152.30},
    {"Date": "2024-08-03", "Stock": "AAPL", "Price": 149.80},
    {"Date": "2024-08-04", "Stock": "AAPL", "Price": 153.40},
    {"Date": "2024-08-05", "Stock": "AAPL", "Price": 155.00},
]

# Write to CSV file
with open("original_stock_data.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Date", "Stock", "Price"])
    writer.writeheader()
    writer.writerows(stock_data)

print("Original CSV file created.")

# Step 2: Simulate the Transfer of the CSV File
shutil.copy("original_stock_data.csv", "transferred_stock_data.csv")
print("CSV file transferred.")

# Step 3: Simulate the MitM Attack
df = pd.read_csv("transferred_stock_data.csv")

# Modify the stock prices by increasing them by 10%
df["Price"] = df["Price"] * 1.1

# Save the modified CSV file
df.to_csv("modified_stock_data.csv", index=False)
print("CSV file modified during transfer.")

# Step 4: Compare the Files
original_df = pd.read_csv("original_stock_data.csv")
modified_df = pd.read_csv("modified_stock_data.csv")

print("\nOriginal CSV Data:")
print(original_df)

print("\nModified CSV Data:")
print(modified_df)
