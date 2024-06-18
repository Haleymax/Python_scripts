import requests
import pandas as pd

from bilibili import save_json_to_file


def convert_to_excel(data):
    # Extract the 'list' key from the data
    data_list = data['data']['list']

    # Filter the data for director_name equals to "黄宏伟"
    filtered_data = [entry for entry in data_list if entry.get('director_name') == '黄宏伟']

    # Convert the filtered data to DataFrame
    df = pd.DataFrame(filtered_data)

    # Write DataFrame to Excel file
    excel_file = "xls/rightrate.xlsx"
    df.to_excel(excel_file, index=False)

    return excel_file

def crawl_data_statistics():
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
    data = {}  # Add your payload data if needed

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

# Example usage:
response_data = crawl_data_statistics()
save_json_to_file(response_data, "json/right.json")
print(response_data)
convert_to_excel(response_data)
