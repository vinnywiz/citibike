# Import standard libraries
import logging

# Import custom libraries
from .load_data import load_data
from .preprocess_data import combine_raw_data

logger = logging.getLogger(__name__)

def run_etl(load_raw=False):
    if load_raw:
        logger.info("Downloading raw data")
        load_data()
        logger.info('Combining raw data')
        combine_raw_data()
    logger.info("Processing Complete")