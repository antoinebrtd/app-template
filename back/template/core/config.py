import json
import logging
import os

config = json.load(open(os.environ.get('CONFIG_FILE', './config/config.json')))

logger = logging.getLogger()
formatter = logging.Formatter('%(process)d %(asctime)s %(name)-12s %(levelname)-8s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

log_level = config.get('log', 'INFO')
if log_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logger = logging.getLogger('template')

version = '0.1.0'
