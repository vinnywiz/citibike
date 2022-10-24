import requests
import zipfile
import os
from io import BytesIO
import yaml

def download_and_extract_zip_file(output_folder, file_url='https://s3.amazonaws.com/tripdata/202001-citibike-tripdata.csv.zip'):
    r = requests.get(file_url, stream=True)
    z = zipfile.ZipFile(BytesIO(r.content))
    z.extractall(output_folder)
    return r.ok

def read_yaml_config_file():
    yaml_path = os.path.join('citi_app','etl', 'config.yaml')
    with open(yaml_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def load_data(begin_year=2021, end_year=2021):
    # Get config variables
    config = read_yaml_config_file()
    raw_output_folder = config['raw_data_path']
    raw_output_path = os.path.join(raw_output_folder)
    # Load individual zipped file
    download_and_extract_zip_file(output_folder=raw_output_path)
