# 第一步：导入包
import requests
# 第二步确定访问的地址，准确爬取
url = 'https://data.bilibili.com/v2/log/web?content_type=pbrequest'
# 模拟服务器发送get请求
res= requests.get(url)
# 返回请求内容
# print(res)  # 返回请求响应码
print(res.status_code)
print(res.headers) # 返回请求头
# 使用encoding转码
res.encoding = 'utf8'
# print(res.text) # 返回页面信息以文本的形式返回源代码，可能打印出的文本为乱码，转码
# 二进制解码  decode
# print(res.content.decode('utf8'))
# print(res.content)  # 打印的内容为二进制内容