import socket
import time
import random

def simulate_weak_network(data):
    # 模拟延迟
    # time.sleep(random.uniform(0.01, 0.02))
    time.sleep(0.001)# 延迟0.1到1秒
    # 模拟丢包
    if random.random() < 0.01:  # 10%的丢包率
        return None
    return data

def handle_client(client_socket):
    request = client_socket.recv(4096)
    if not request:
        return

    # 打印请求内容
    print("=== Request ===")
    print(request.decode('utf-8', errors='ignore'))  # 解码为UTF-8，忽略无法解码的部分
    print("===============")

    # 模拟弱网效果
    request = simulate_weak_network(request)
    if request is None:
        print("Packet lost (simulated)")
        client_socket.close()
        return

    # 解析请求的目标地址和端口
    # 这里假设是HTTP请求，目标地址是"www.example.com:80"
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect(("www.example.com", 80))  # 替换为实际目标地址
    remote_socket.send(request)

    # 接收目标服务器的响应
    response = remote_socket.recv(4096)
    response = simulate_weak_network(response)
    if response is None:
        print("Packet lost (simulated)")
        remote_socket.close()
        client_socket.close()
        return

    # 打印响应内容
    print("=== Response ===")
    print(response.decode('utf-8', errors='ignore'))  # 解码为UTF-8，忽略无法解码的部分
    print("================")

    # 将响应返回给客户端
    client_socket.send(response)
    client_socket.close()
    remote_socket.close()

def start_proxy(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Proxy server started on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_proxy()