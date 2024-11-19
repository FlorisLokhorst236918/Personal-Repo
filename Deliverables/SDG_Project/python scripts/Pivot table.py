import pandas as pd

# Load the dataset
file_path = "C:\\2024-25A-FAI1-ADSAI--FlorisLokhorst236918\\IMHE data\\fact_table.csv"  # Update this with your file path
df = pd.read_csv(file_path)

# Check for duplicates
duplicate_rows = df.duplicated(subset=['location_id', 'age_id', 'sex_id', 'year', 'metric_name'], keep=False)
print(f"Number of duplicates: {duplicate_rows.sum()}")

# Pivot the data using the 'first' method
df_pivoted = df.pivot_table(
    index=['location_id', 'age_id', 'sex_id', 'year'],
    columns='metric_name',
    values='val',
    aggfunc='first'  # This keeps the value as is
).reset_index()

# Save the pivoted data to a new CSV
df_pivoted.to_csv("Simplified_Pivoted_Fact_Table.csv", index=False)
print("Data pivoted and saved as 'Simplified_Pivoted_Fact_Table.csv'")
