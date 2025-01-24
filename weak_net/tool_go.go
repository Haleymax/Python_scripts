package main

import (
	"fmt"
	"io"
	"log"
	"math/rand"
	"net"
	"time"
)

// simulateWeakNetwork 模拟弱网效果，包括延迟和丢包
func simulateWeakNetwork(data []byte) []byte {
	// 模拟延迟
	time.Sleep(time.Duration(rand.Intn(100)+100) * time.Millisecond) // 延迟100ms到200ms

	// 模拟丢包
	if rand.Float32() < 0.01 { // 10%的丢包率
		return nil
	}
	return data
}

// handleClient 处理客户端连接
func handleClient(clientConn net.Conn) {
	defer clientConn.Close()

	// 读取客户端请求
	request := make([]byte, 4096)
	n, err := clientConn.Read(request)
	if err != nil {
		log.Println("Error reading from client:", err)
		return
	}
	request = request[:n]

	// 打印请求内容
	fmt.Println("=== Request ===")
	fmt.Println(string(request))
	fmt.Println("===============")

	// 模拟弱网效果
	request = simulateWeakNetwork(request)
	if request == nil {
		log.Println("Packet lost (simulated)")
		return
	}

	// 连接到目标服务器
	remoteConn, err := net.Dial("tcp", "www.example.com:80")
	if err != nil {
		log.Println("Error connecting to remote server:", err)
		return
	}
	defer remoteConn.Close()

	// 发送请求到目标服务器
	_, err = remoteConn.Write(request)
	if err != nil {
		log.Println("Error sending request to remote server:", err)
		return
	}

	// 读取目标服务器的响应
	response := make([]byte, 4096)
	n, err = remoteConn.Read(response)
	if err != nil && err != io.EOF {
		log.Println("Error reading response from remote server:", err)
		return
	}
	response = response[:n]

	// 模拟弱网效果
	response = simulateWeakNetwork(response)
	if response == nil {
		log.Println("Packet lost (simulated)")
		return
	}

	// 打印响应内容
	fmt.Println("=== Response ===")
	fmt.Println(string(response))
	fmt.Println("================")

	// 将响应返回给客户端
	_, err = clientConn.Write(response)
	if err != nil {
		log.Println("Error sending response to client:", err)
		return
	}
}

// startProxy 启动代理服务器
func startProxy(host string, port int) {
	listener, err := net.Listen("tcp", fmt.Sprintf("%s:%d", host, port))
	if err != nil {
		log.Fatalf("Error starting proxy server: %v", err)
	}
	defer listener.Close()

	log.Printf("Proxy server started on %s:%d\n", host, port)

	for {
		clientConn, err := listener.Accept()
		if err != nil {
			log.Println("Error accepting connection:", err)
			continue
		}
		log.Printf("Connection from %s\n", clientConn.RemoteAddr())
		go handleClient(clientConn)
	}
}

func main() {
	rand.Seed(time.Now().UnixNano()) // 初始化随机数种子
	startProxy("0.0.0.0", 9999)
}