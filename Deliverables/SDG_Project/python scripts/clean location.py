import pandas as pd

# Define file paths
main_file = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\Simplified_Pivoted_Fact_Table_processed.csv"  # Path to your main CSV file
location_id_file = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\locations.csv"  # Updated path to the location ID reference file
output_file = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\Filtered_Simplified_Pivoted_Fact_Table.csv"  # Path to save the filtered data

# Load the location ID reference file with a different encoding and delimiter
location_ids_df = pd.read_csv(location_id_file, encoding='ISO-8859-1', delimiter=';')
location_ids_df.columns = location_ids_df.columns.str.strip()  # Strip whitespace from all column names

# Check for the exact name of the location ID column
print("Location ID DataFrame columns:", location_ids_df.columns)

# Make sure the 'location_id' column is treated as a string
if 'location_id' in location_ids_df.columns:
    location_ids_df['location_id'] = location_ids_df['location_id'].astype(str).str.strip()
else:
    print("Error: 'location_id' column not found in location_ids_df.")
    exit()

# Load the main file
main_df = pd.read_csv(main_file)

# Ensure consistency in `location_id` column format in the main file as well
main_df.columns = main_df.columns.str.strip()  # Strip whitespace from all column names

if 'location_id' in main_df.columns:
    main_df['location_id'] = main_df['location_id'].astype(str).str.strip()
else:
    print("Error: 'location_id' column not found in main_df.")
    exit()

# Filter main data to keep only rows where `location_id` is in the reference list
filtered_df = main_df[main_df['location_id'].isin(location_ids_df['location_id'])]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved as: {output_file}")
