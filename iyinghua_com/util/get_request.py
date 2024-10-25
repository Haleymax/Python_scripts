import requests

from util.logger import logger


class Request:
    def __init__(self, url):
        self.respon = None
        self.headers = {}
        self.base_url = url

    def set_user_agent(self, user_agent):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "9151_3587_58.33.9.194=1; 9152_3602_58.33.9.194=1; Hm_lvt_9388bb65e632be68b8e346d1a6e3ee76=1729846523; HMACCOUNT=6A67E1A5B93D177D; qike123=%u6D77%u8D3C%u738B1120^http%3A//www.iyinghua.com//v/2-1120.html_$_|; Hm_lvt_2486aa1b2311df5424f620de76a0e4e3=1729846666; Hm_lpvt_2486aa1b2311df5424f620de76a0e4e3=1729846666; 9151_3900_58.33.9.194=1; 9152_3911_58.33.9.194=1; richviews_9151=K11tkBbJ8SKtnVX2AWLhogwfw%252FwI1ESqate%252FxeLfguOi6i8z5ltvMcpL%252BZ0e8RbDSFAsr7SQ26vxxL%252F3EvmUvF5WwsUCVTiaazJo7FmiSdM4DvTERwvU7r8Hp%252Bv20M3rxtGScN%252FJ11CW9mUp260cZyJYEQ86WSB8%252BQqCUyHqFj7sD5J0SkFj3GgU%252FoDSEBrIcmcYl5%252Bw0VbvrZcLGc3z6tpmJCy46fxBwg%252BjXTErPKVRXopLSmLZG8yjNH1PwpPPiEdFOreppbQSvA3J%252FY9ykm0B3Wn75mRp3tqPCsdq6q%252BdpQmjOz8Uksg2DLSok65McYNwDzf%252BcaZVQd3HFliZOQ%253D%253D; 9151_3926_58.33.9.194=1; beitouviews_9152=RqkVFvkF8F%252FbFiBP5IoDUfnnyfmPTCfmsuj8H98DPhd1UWPaNqDSAWRdxSaMplhj8hbCoAvY3mNPz%252FYF2XQOFCEiSSC897eSoyofij2npCnKm65tWwqv4AI%252BHDno0BLJfqMDuhhTJPNp0doBgwdm6ql7NNMt06skBQdZI29xeuxK0SPV7irk8UGfwgh2aIPZ2pLeSDmL7vmRb7XZ019fbA9yDilTtMYVGofFUJ%252BINprkRChVWcQkiLucsMueSNx%252F940L60v2SWl%252FTHrF50sRQd7qlMItL2TYCDjtuuDXxSCNGYKUuRt1RrBfYAtnLDg8Gn3G3BBnN%252FGssBFXm%252FAV7A%253D%253D; 9152_3927_58.33.9.194=1; Hm_lpvt_9388bb65e632be68b8e346d1a6e3ee76=1729850132",
            "Host": "www.iyinghua.com",
            "If-Modified-Since": "Fri, 25 Oct 2024 04:16:05 GMT",
            "If-None-Match":'W/"671b1b85-d8c9"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }

    def get_request_base_info(self):
        self.respon = requests.get(self.base_url, headers=self.headers, verify=False)
        self.respon.encoding = 'utf-8'
        logger.info("initiate GET request to obtain the page data")