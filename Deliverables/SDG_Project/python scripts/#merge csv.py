import pandas as pd
import glob
import os

# Path where all CSV files are located
file_path = "C:\\2024-25A-FAI1-ADSAI--FlorisLokhorst236918\\IMHE data"

csv_files = glob.glob(os.path.join(file_path, "*.csv"))

combined_df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("fact_table.csv", index=False)

print("CSV files combined successfully into 'combined_output.csv'!")
input("press enter to exit")