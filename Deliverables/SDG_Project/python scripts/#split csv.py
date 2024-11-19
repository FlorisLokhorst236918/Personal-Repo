#split csv 
import pandas as pd
# Load the original dataset
file_path = "C:\\2024-25A-FAI1-ADSAI--FlorisLokhorst236918\\IMHE data\\combined_output.csv"  # Update this with the actual path to your file
df = pd.read_csv(file_path)

# Define the columns you want to keep in your fact table
fact_columns = ['location_id', 'sex_id', 'age_id', 'year', 'metric_name', 'val', 'upper', 'lower']  # Adjust as needed

# Filter the dataset to only include the fact table columns
fact_df = df[fact_columns]

# Get a list of unique years in the dataset
years = fact_df['year'].unique()

# Loop through each year and export to a separate CSV
for year in years:
    # Filter the dataset for the current year
    df_year = fact_df[fact_df['year'] == year]
    
    # Save to a CSV file named after the year
    output_filename = f"Fact_Table_{year}.csv"
    df_year.to_csv(output_filename, index=False)
    print(f"Data for year {year} saved as {output_filename}")

print("Fact table data successfully split and saved by year.")
