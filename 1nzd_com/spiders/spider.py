import re

import requests

from config.read_config import read_config
from spiders.regex import singer_page_regex, song_url_regex, music_page_url_regex, input_pattern_regex
from util.download import start_download_thread
from util.get_request import Request
from util.logger import logger


class MusicWeb(Request):
    def __init__(self, url):
        super().__init__(url)
        self.music_page_url_dick = {}
        self.mp3_link_dick = {}
        self.music_page_url = None
        self.name = None

    def search_singer(self, singer):
        self.singer_url = f"{self.base_url}/search?ac={str(singer)}"

    def get_singer_page_info(self):
        self.respon = requests.get(self.singer_url, headers=self.headers)

    def add_music_link(self, name, url):
        logger.info(f"get song:{name} , url:{url}")
        self.music_page_url_dick[name] = self.base_url+ url

    def get_all_music_page_link(self):
        search_result_page = singer_page_regex.finditer(self.respon.text)
        for it in search_result_page:
            child_page = it.group()
            result2 = song_url_regex.findall(child_page)
            ul_content = result2[0]
            link_and_name_pattern = r'<a href="([^"]+)".*?-(.*?)</a>'
            link_and_name_matches = re.findall(link_and_name_pattern, ul_content)
            for link, song_name in link_and_name_matches:
                self.add_music_link(song_name, link)

    def get_all_music_link(self):
        for name, url in self.music_page_url_dick.items():
            self.music_page_url = url
            self.name = name
            self.get_music_link()

    def get_music_link(self):
        self.respon = requests.get(self.music_page_url, headers=self.headers)
        music_link =input_pattern_regex.findall(self.respon.text)[0]
        self.mp3_link_dick[self.name] = music_link
        logger.info(f"start download {self.name}")
        start_download_thread(music_link, self.name)

def star_spider():
    logger.info("___________开始爬虫___________")
    spider = MusicWeb(read_config.get_baseurl())
    singer = input("请输入歌手 : ")
    spider.search_singer(singer)
    spider.get_singer_page_info()
    spider.get_all_music_page_link()
    spider.get_all_music_link()
    logger.info("___________爬取完毕___________")

if __name__ == '__main__':
    star_spider()