import requests

from util.logger import logger


class Request:
    def __init__(self, url):
        self.respon = None
        self.headers = {}
        self.base_url = url

    def set_user_agent(self, user_agent):
        self.headers["user-agent"] = user_agent

    def get_request_base_info(self):
        self.respon = requests.get(self.base_url, headers=self.headers)
        logger.info("initiate GET request to obtain the page data")