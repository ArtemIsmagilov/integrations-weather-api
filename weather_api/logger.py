import logging

from weather_api.settings import conf

logging.basicConfig()

logger = logging.getLogger("weather_api")
logger.setLevel(conf.LOG_LEVEL)
