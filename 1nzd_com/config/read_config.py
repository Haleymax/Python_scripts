import os

import yaml

from settings.all_path import config_path
from util.logger import logger

config_file = os.path.join(config_path, "config.yml")

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

class ReadConfig:
    def __init__(self):
        self.data = load_yaml(config_file)

    def get_baseurl(self):
        logger.info("读取目标网站的url")
        config = self.data["spider"]
        return str(config['target_url'])

    def get_user_agent(self):
        logger.info("读取浏览器用户代理")
        config = self.data["spider"]
        return str(config['agent'])


read_config = ReadConfig()
