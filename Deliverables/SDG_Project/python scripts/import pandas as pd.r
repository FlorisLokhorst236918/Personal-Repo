import pandas as pd

# Define file paths
countries_file_path = "C:\\2024-25A-FAI1-ADSAI--FlorisLokhorst236918\\locations.xlsx"  # Replace with the actual file path
pivoted_table_file_path = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\Simplified_Pivoted_Fact_Table.csv"  # Replace with the actual file path
output_file_path = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project"  # Define output file path

# Load the countries with IDs table
countries_with_ids = pd.read_csv(countries_file_path)

# Load the large `simplified_pivoted_table`
pivoted_table = pd.read_csv(pivoted_table_file_path)

# Extract the list of relevant IDs from the countries table
relevant_ids = countries_with_ids['location_id'].unique()

# Filter the pivoted_table to keep only rows with IDs in the relevant_ids list
filtered_table = pivoted_table[pivoted_table['location_id'].isin(relevant_ids)]

# Save the filtered table
filtered_table.to_csv(output_file_path, index=False)

print(f"Filtered table saved to {output_file_path}")
