import pandas as pd

# Define file path for location ID file
location_id_file = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\locations.csv"  # Adjust to your file path

# Load the location ID file
location_ids_df = pd.read_csv(location_id_file)

# Print column names to see what's actually present
print(location_ids_df.columns)
