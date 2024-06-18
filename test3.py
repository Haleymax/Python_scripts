import requests

def crawl_portal_notice():
    url = "https://oa.cqie.edu.cn/sys/portal/sys_portal_notice/sysPortalNotice.do?method=getPortalNotice&s_ajax=true"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://oa.cqie.edu.cn",
        "Referer": "https://oa.cqie.edu.cn/sys/portal/page.jsp",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    # 发送POST请求
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return response.text  # 返回响应文本
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

# 示例用法：

#response_text = crawl_portal_notice()
    #print(response_data)


response_text = crawl_portal_notice()
print(response_text)
