import requests

from config.read_config import read_config
from spiders.regex import singer_page_regex
from util.get_request import Request


class MusicWeb(Request):
    def __init__(self, url):
        super().__init__(url)
        self.music_url = []

    def search_singer(self, singer):
        self.singer_url = f"{self.base_url}/search?ac={str(singer)}"
        print(self.singer_url)

    def get_singer_page_info(self):
        self.respon = requests.get(self.singer_url, headers=self.headers)

    def music_urls(self, url):
        self.music_url.append(url)


def execute():
    spider = MusicWeb(read_config.get_baseurl())
    spider.search_singer("周杰伦")
    spider.get_singer_page_info()
    result1 = singer_page_regex.finditer(spider.respon.text)
    for it in result1:
        print(it.group('ul'))


execute()