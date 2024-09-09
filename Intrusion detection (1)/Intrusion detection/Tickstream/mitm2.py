import shutil
import pandas as pd


shutil.copy("Tickstream\AAPL.csv", "transferred_AAPL.csv")
print("AAPL.csv file transferred.")


df = pd.read_csv("transferred_AAPL.csv")

df["Price"] = df["Price"] * 1.1

df.to_csv("modified_AAPL.csv", index=False)
print("AAPL.csv file modified during transfer.")

original_df = pd.read_csv("AAPL.csv")
modified_df = pd.read_csv("modified_AAPL.csv")

print("\nOriginal AAPL.csv Data:")
print(original_df)

print("\nModified AAPL.csv Data:")
print(modified_df)
