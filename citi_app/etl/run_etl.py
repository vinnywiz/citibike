import logging

from yaml import load
from .load_data import load_data

def run_etl():
    load_data()