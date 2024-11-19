import os
import subprocess

# Define the table and date column details
table_name = "Simplified_Pivoted_Fact_Table"
date_column = "year"  # assuming "year" contains integer values for each year
output_folder = "C:\\Users\\Flori\\OneDrive\\Bureaublad\\Project\\temp"  # Replace with your output folder path
dax_studio_path = "C:\\Program Files\\DAX Studio\\dscmd.exe"  # Path to DAX Studio CLI executable

# Define the start and end years for export
start_year = 1990
end_year = 2021

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through each year and run the query in DAX Studio CLI
for year in range(start_year, end_year + 1):
    # Construct the DAX query for the specific year, filtering by the "year" column
    query = f"""
    EVALUATE
    FILTER(
        {table_name},
        {table_name}[{date_column}] = {year}
    )
    """
    
    # Save the query to a temporary .dax file
    query_file = f"{output_folder}/query_{year}.dax"
    with open(query_file, "w") as file:
        file.write(query)
    
    # Define the output file for the year
    output_file = os.path.join(output_folder, f"{table_name}_{year}.csv")
    
    # Run DAX Studio CLI to execute the query and save the output to CSV
    subprocess.run([
        dax_studio_path,
        "/Q", query_file,           # The query file
        "/O", output_file,           # Output file for CSV
        "/F", "CSV"                  # Specify CSV format
    ], check=True)
    
    # Clean up the temporary query file
    os.remove(query_file)
    
    print(f"Exported data for {year} to {output_file}")
