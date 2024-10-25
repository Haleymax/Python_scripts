import os
from distutils.command.config import config

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
        config_data = self.data["spider"]
        return str(config_data['target_url'])

    def get_user_agent(self):
        logger.info("读取浏览器用户代理")
        config_data = self.data["spider"]
        return str(config_data['agent'])

    def get_mongodb_url(self):
        logger.info("读取mongodb的url")
        config_data = self.data["mongodb"]
        return str(config_data['url'])

    def get_mongodb_database(self):
        logger.info("读取mongodb的数据库")
        config_data = self.data["mongodb"]
        return str(config_data['database'])

    def get_mongodb_collection(self):
        logger.info("读取collection")
        config_data = self.data["mongodb"]
        return str(config_data['collection'])

    def get_mysql_host(self):
        logger.info("读取MySQL主机地址")
        config_data = self.data["mysql"]
        return str(config_data['host'])

    def get_mysql_port(self):
        logger.info("读取MySQL的端口")
        config_data = self.data["mysql"]
        return str(config_data['port'])

    def get_mysql_user(self):
        logger.info("读取MySQL用户名")
        config_data = self.data["mysql"]
        return str(config_data['user'])

    def get_mysql_password(self):
        logger.info("读取MySQL密码")
        config_data = self.data["mysql"]
        return str(config_data['password'])

    def get_mysql_db(self):
        logger.info("读取MySQL数据库名")
        config_data = self.data["mysql"]
        return str(config_data['database'])

read_config = ReadConfig()
