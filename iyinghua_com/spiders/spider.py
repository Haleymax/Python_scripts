import requests

from util.logger import logger


def star_spider():
    # logger.info("___________开始爬虫___________")
    #
    # url = "https://lf16-fe.resso.me/obj/tos-alisg-ve-0051c001-sg/oINAievCZKzCfBwdio0fkfbUAEeiAkzBwmeADfB?filename=1.mp4"
    # header = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
    # respone = requests.get(url, headers=header)
    #
    # if respone.status_code == 200:
    #     file_name = "test.mp4"
    #     try:
    #         with open(file_name, 'wb') as f:
    #             f.write(respone.content)
    #         logger.info(f"{file_name} ,下载成功")
    #     except Exception as e:
    #         logger.warning(f"write file faild because : {e}")
    # else:
    #     logger.warning("fail link")









    logger.info("___________爬取完毕___________")

if __name__ == '__main__':
    star_spider()