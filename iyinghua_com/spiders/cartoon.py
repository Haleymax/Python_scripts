from iyinghua_com.config.read_config import read_config
from iyinghua_com.util.get_request import Request


class CartoonWeb(Request):
    def __init__(self):
        super().__init__("http://www.iyinghua.com/show/5095.html")
        self.name = None






cartoon = CartoonWeb()

cartoon.set_user_agent(read_config.get_user_agent())
cartoon.get_request_base_info()
print(cartoon.respon.text)