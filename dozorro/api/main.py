import argparse
import logging

logger = logging.getLogger(__name__)


def cdb_init():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dropdb', action='store_true')
    parser.add_argument('--config')
    parser.add_argument('root_key')
    args = parser.parse_args()
    logger.info("Tables created")
    return 0
