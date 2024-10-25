import pymongo

from config.read_config import read_config
from util.logger import logger


class MongoClient:
    def __init__(self, url, database):
        try:
            self.client = pymongo.MongoClient(url)
            self.db = self.client[database]
            logger.info('successfully connected to MongoDB')
        except Exception as e:
            logger.error(e)






my_mongo_client = MongoClient(read_config.get_mongodb_url(), read_config.get_mongodb_database())