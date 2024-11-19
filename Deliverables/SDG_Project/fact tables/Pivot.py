import pandas as pd

# Load the dataset
file_path = "C:\\2024-25A-FAI1-ADSAI--FlorisLokhorst236918\\IMHE data\\fact_table.csv"  # Replace with your file path
df = pd.read_csv(file_path)

# Pivot the data so 'metric_name' values become columns
df_pivoted = df.pivot_table(index=['location_id', 'age_id', 'sex_id', 'year'],
                            columns='metric_name',
                            values='val').reset_index()

# Save the pivoted data to a new CSV
df_pivoted.to_csv("Fact_Table_Pivoted.csv", index=False)

print("Data successfully pivoted and saved to 'Fact_Table_Pivoted.csv'")
