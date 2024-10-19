import os

from read_data import read_data
from settings.all_path import config_path
from util.logger import logger

config_file = os.path.join(config_path, "config.yml")

def get_data_by_yaml(yaml_file_name):
    try:
        data_file_path = os.path.join(config_path, yaml_file_name)
        yaml_data = read_data.load_yaml(data_file_path)
    except Exception as ex:
        logger.warning(f"fail get data because : {ex}")
    else:
        return yaml_data

class ReadConfig:
    def __init__(self):
        self.data = read_data.load_ini(config_file)

    def get_mongourl(self):
        logger.info("读取 mogo 连接地址")
        config = self.data["mongoDB"]
        return config['mongourl']

    def get_database(self):
        logger.info("读取 database")
        config = self.data["mongoDB"]
        return config['database']



read_config = ReadConfig()
