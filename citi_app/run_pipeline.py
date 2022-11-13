# Import Standard Libraries
import logging

# Import Custom Libraries
from citi_app.etl import run_etl

logger = logging.getLogger(__name__)

def run_pipeline(load_raw=False):
    #logging.basicConfig(filename='sample.log', level=logging.INFO)
    logging.basicConfig(filename='logging.log', format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.INFO)
    logger.info("Running ETL")
    run_etl(load_raw=load_raw)
    logging.shutdown()