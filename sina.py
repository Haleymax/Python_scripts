import requests

url = 'https://www.sina.com.cn/?'

# 搜索关键字
key = '0000'
# 设置请求头和数据
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4449.0 Safari/537.36'
}

params ={
    'q': key,
    'c': 'news',
    'from': 'inde'
}

res = requests.get(url, headers=header, data=params )
# 输出结果,document.charset控制台检查编码结果
res.encoding = 'utf8'
print(res.text)
