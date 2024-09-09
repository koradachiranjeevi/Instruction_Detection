import shutil
import pandas as pd
import random
import numpy as np

# Step 1: Copy the original file to simulate a transfer
shutil.copy("Tickstream/AAPL.csv", "transferred_AAPL.csv")
print("AAPL.csv file transferred.")

# Step 2: Load the transferred CSV file
df = pd.read_csv("transferred_AAPL.csv")

# Parameters for the attack
num_points_to_modify = 6230  # Number of data points to modify
modification_range = 0.05  # The percentage range for modification (e.g., +/- 5%)
columns_to_modify = ['Price']  # Column to modify (you can add more columns if needed)

# Step 3: Randomly select rows to modify
rows_to_modify = sorted(random.sample(range(len(df)), num_points_to_modify))

# Step 4: Introduce random timing (irregular intervals between modifications)
random_intervals = np.random.randint(1, 5, size=num_points_to_modify-1)
rows_to_modify_with_intervals = [rows_to_modify[0]]

for interval in random_intervals:
    next_row = rows_to_modify_with_intervals[-1] + interval
    if next_row < len(df):
        rows_to_modify_with_intervals.append(next_row)

# Step 5: Modify the selected rows with randomized changes
for row in rows_to_modify_with_intervals:
    for column in columns_to_modify:
        original_value = df.at[row, column]
        modification = original_value * random.uniform(-modification_range, modification_range)
        df.at[row, column] = original_value + modification

# Step 6: Save the modified DataFrame to a new CSV file
df.to_csv("mdfapl.csv", index=False)

# Verify that the file was saved correctly
print("\nModified AAPL.csv file saved.")

# Step 7: Load and compare the original and modified data
original_df = pd.read_csv("Tickstream/AAPL.csv")
modified_df = pd.read_csv("mdfapl.csv")

print("\nOriginal AAPL.csv Data:")
print(original_df.head())  # Display only the first few rows for brevity

print("\nModified AAPL.csv Data:")
print(modified_df.head())  # Display only the first few rows for brevity

# Optional: Highlight the modified rows for better visualization
modified_rows = modified_df.loc[rows_to_modify_with_intervals]
print("\nRows modified during the attack:")
print(modified_rows)
