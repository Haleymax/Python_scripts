import os.path
import threading

import requests

from all_path import data_path
from util.logger import logger


def download(url, name):
    respone = requests.get(url)
    if respone.status_code == 200:
        file_name = f"{name}.mp3"
        file_path = os.path.join(data_path,file_name)
        with open(file_path, 'wb') as f:
            f.write(respone.content)
        logger.info(f"{name} ,下载成功")
    else:
        logger.warning("fail link")


def start_download_thread(url, name):
    thread = threading.Thread(target=download, args=(url, name))
    thread.start()