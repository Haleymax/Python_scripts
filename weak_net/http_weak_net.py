from flask import Flask, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time
import requests

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["1 kb/s"]  # 设置默认带宽限制
)

# 设置延迟
@app.route('/<path:url>', methods=['GET', 'POST'])
@limiter.limit("1 KB/s")  # 每秒 1KB 的带宽限制
def proxy(url):
    # 模拟延迟
    time.sleep(2)  # 延迟 2 秒

    # 转发请求
    if request.method == 'POST':
        response = requests.post(f'http://{url}', data=request.data, headers=request.headers)
    else:
        response = requests.get(f'http://{url}', headers=request.headers)

    # 返回响应
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3322)
