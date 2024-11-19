import pandas as pd

# Define the file paths
input_file = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\temp\\Simplified_Pivoted_Fact_Table.csv"  # Path to your exported CSV file
output_file = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\temp\\Simplified_Pivoted_Fact_Table_processed.csv"  # Path for the fixed file

# Load the file without headers
df = pd.read_csv(input_file, header=None)

# Set the first row as the header
df.columns = df.iloc[0]  # Promote the first row to be the header
df = df[1:].reset_index(drop=True)  # Drop the first row from the data

# Save the updated DataFrame to a new file
df.to_csv(output_file, index=False)

print(f"Processed file saved as: {output_file}")
