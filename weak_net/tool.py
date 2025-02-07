import socket
import time
import random

# 模拟带宽函数，单位为 kbps
def simulate_bandwidth(data, bandwidth_kbps):
    data_size = len(data)
    time_needed = (data_size * 8) / (bandwidth_kbps * 1024)
    chunk_size = 10240
    start_time = time.time()
    sent = 0
    while sent < data_size:
        chunk = data[sent:sent + chunk_size]
        if chunk:
            elapsed_time = time.time() - start_time
            expected_time = (sent * 8) / (bandwidth_kbps * 1024)
            if elapsed_time < expected_time:
                time.sleep(expected_time - elapsed_time)
            sent += len(chunk)
    return data

# 模拟弱网环境（延迟和丢包）
def simulate_weak_network(data):
    # 模拟延迟，0.1 到 1 秒
    time.sleep(random.uniform(0.1, 1))
    # 模拟丢包，1% 的丢包率
    if random.random() < 0.01:
        return None
    return data

# 处理客户端请求
def handle_client(client_socket, bandwidth_kbps):
    try:
        request = client_socket.recv(4096)
        if not request:
            return

        # 打印接收到的请求内容
        print(f"Received request:\n{request.decode('utf-8', errors='ignore')}")

        # 模拟弱网效果
        request = simulate_weak_network(request)
        if request is None:
            print("Packet lost (simulated)")
            client_socket.close()
            return

        # 解析请求的目标地址和端口
        request_lines = request.decode('utf-8', errors='ignore').splitlines()
        host = None
        port = 80
        for line in request_lines:
            if line.lower().startswith('host:'):
                host = line.split(':')[1].strip()
                if len(line.split(':')) > 2:
                    port = int(line.split(':')[2].strip())
                break

        # 打印解析得到的 host 和 port
        print(f"Parsed host: {host}, port: {port}")

        if host is None:
            print("Failed to parse host from request")
            client_socket.close()
            return

        # 创建到目标服务器的连接
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            remote_socket.connect((host, port))
            # 模拟带宽发送请求
            simulate_bandwidth(request, bandwidth_kbps)
            remote_socket.sendall(request)
        except socket.error as e:
            print(f"Failed to connect to target server: {e}")
            client_socket.close()
            remote_socket.close()
            return

        # 接收目标服务器的响应
        response = b""
        while True:
            chunk = remote_socket.recv(4096)
            if not chunk:
                break
            response += chunk

        response = simulate_weak_network(response)
        if response is None:
            print("Packet lost (simulated)")
            remote_socket.close()
            client_socket.close()
            return

        # 模拟带宽返回响应
        simulate_bandwidth(response, bandwidth_kbps)
        # 将响应返回给客户端
        client_socket.sendall(response)

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
        remote_socket.close()

# 启动代理服务器
def start_proxy(host='0.0.0.0', port=3322, bandwidth_kbps=128):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Proxy server started on {host}:{port} with bandwidth: {bandwidth_kbps} kbps")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket, bandwidth_kbps)

if __name__ == "__main__":
    start_proxy()
