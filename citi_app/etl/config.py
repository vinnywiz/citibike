import os
import yaml

def read_yaml_config_file():
    yaml_path = os.path.join('citi_app','etl', 'config.yaml')
    with open(yaml_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config