import pandas as pd

# Load CSV
df = pd.read_csv("datasets/sample_sales.csv")

# Basic inspection
print("Number of rows:", len(df))
print("Columns:", df.columns.tolist())
print("\nPreview:")
print(df.head())
