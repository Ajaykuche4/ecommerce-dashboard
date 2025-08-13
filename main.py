import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_dataset.csv")

# Make a copy for cleaning
df_clean = df.copy()

# Check for missing values
print("\nMissing Values in Each Column:")
print(df_clean.isnull().sum())

# Convert Order Date to datetime format
df_clean['Order Date'] = pd.to_datetime(df_clean['Order Date'], errors='coerce')

# Remove duplicates
before_duplicates = len(df_clean)
df_clean.drop_duplicates(inplace=True)
after_duplicates = len(df_clean)

# Remove invalid prices
df_clean = df_clean[(df_clean['Unit Price'] > 0) & (df_clean['Total Amount'] > 0)]

# Summary of cleaning
print("\nSummary of Cleaning:")
print(f"Duplicates Removed: {before_duplicates - after_duplicates}")
print(f"Final Rows: {len(df_clean)}")

# Save cleaned dataset
df_clean.to_csv("ecommerce_dataset_clean.csv", index=False)
print("\nCleaned dataset saved as 'ecommerce_dataset_clean.csv'")
