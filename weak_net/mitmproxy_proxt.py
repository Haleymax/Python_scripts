from mitmproxy import http
import random
import time

# 设置延迟和丢包比例
DELAY = 5  # 延迟 500 毫秒
LOSS_RATE = 0.01  # 10% 的丢包率

def request(flow: http.HTTPFlow) -> None:
    # 模拟延迟
    time.sleep(DELAY)

    # 模拟丢包
    if random.random() < LOSS_RATE:
        flow.response = http.Response.make(
            503,  # HTTP状态码
            b"Service Unavailable",  # 响应内容
            {"Content-Type": "text/plain"}  # 响应头
        )



def response(flow: http.HTTPFlow) -> None:
    # 可以在这里处理响应
    pass
