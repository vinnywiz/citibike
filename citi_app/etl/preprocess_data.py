# Import standard libraries
import pandas as pd
import os
import glob

# Import custom libraries
from .config import read_yaml_config_file

def read_files_to_pandas(filenames):
    lis =[]
    for filename in filenames:
        df = pd.read_csv(filename)
        lis.append(df)
    
    all_files_df = pd.concat(lis, axis=0, ignore_index=True)
    return all_files_df

def combine_raw_data():
    # Loading configurations
    config = read_yaml_config_file()
    input_folder = config['raw_data_path'] 
    output_folder = config['processed_data_path']
    combine_file_name = config['combined_file_name']
    input_path = os.path.join(input_folder)
    output_path = os.path.join(output_folder, combine_file_name)
    # Checking if folders exist
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    # Listing & combining files
    citi_files = glob.glob(os.path.join(input_path, "*.*"))
    citi_df = read_files_to_pandas(citi_files)
    citi_df.to_csv(output_path, index=False)