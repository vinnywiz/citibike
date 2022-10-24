from citi_app.etl import run_etl
import logging

logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("Running ETL")
    run_etl()