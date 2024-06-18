import pandas as pd
import requests


def convert_to_excel(data):
    # Extracting the 'list' key from the data
    data_list = data['data']['list']

    # Converting the list of dictionaries to a DataFrame
    df = pd.DataFrame(data_list)

    # Writing DataFrame to Excel file
    excel_file = "xls/data.xlsx"
    df.to_excel(excel_file, index=False)

    return excel_file
def crawl_game_task_target_list():
    url = "http://assist.qiming321.cn:8001/api/gameTask/getGameTaskTargetList"
    url = "http://assist.qiming321.cn:8001/api/dataStatistics/queryAbnormalRate"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "Origin": "http://assist.qiming321.cn:8001",
        "Referer": "http://assist.qiming321.cn:8001/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "X-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVVUlEIjoiYWM4YjJkMmItMGVhNi00YzcxLTk1OTAtNmQ5ZjE0MDZjMjc2IiwiSUQiOjI0LCJVc2VybmFtZSI6Imhod2VpMDQxMiIsIk5pY2tOYW1lIjoi6buE5a6P5LyfIiwiQXV0aG9yaXR5SWQiOjIwNDgsIkJ1ZmZlclRpbWUiOjg2NDAwLCJleHAiOjE3MTY2NDY5MDQsImlzcyI6InFtUGx1cyIsIm5iZiI6MTcxMzIzMDU1MH0.Na8VCxlnfK-3M8XHLTQxVbrTX4Dfqcyn_XWU_pH-4Q0",
        "X-User-Id": "24"
    }
    payload = {
        'Page': 1,  # 根据实际需要设置Page参数的值
        'PageSize': 30  # 根据实际需要设置PageSize参数的值
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # 如果请求失败，则抛出异常
        # 获取响应内容
        data = response.json()
        excel_file = convert_to_excel(data)
        print("Excel file generated:", excel_file)
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None



# 测试爬虫并将数据保存到 Excel 文件
if __name__ == "__main__":
    response_data = crawl_game_task_target_list()
