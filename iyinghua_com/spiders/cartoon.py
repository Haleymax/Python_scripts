from frame.util.get_request import Request


class CartoonWeb(Request):
    def __init__(self):
        super().__init__()
        self.name = None