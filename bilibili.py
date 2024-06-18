import os
import json
import requests

def crawl_bilibili_fanju():
    url = "https://api.bilibili.com/pgc/season/index/result?st=1&order=2&season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page=1&season_type=1&pagesize=20&type=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.bilibili.com/"
    }

    try:
        response = requests.get(url, headers=headers)  # Remove json=data here
        response.raise_for_status()  # Raise an HTTPError for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def crawl_bilibili_saisi():
    url = "https://api.bilibili.com/x/esports/season/recommend?csrf=e27282fce004ac3703f0a4ca76ee2b0c&platform=2&size=6"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.bilibili.com/"
    }

    try:
        response = requests.get(url, headers=headers)  # Remove json=data here
        response.raise_for_status()  # Raise an HTTPError for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def save_json_to_file(json_data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        print("JSON data has been successfully saved to", file_path)
    except Exception as e:
        print("An error occurred while saving JSON data:", str(e))

# Example usage:
#response_data = crawl_bilibili_fanju()  #获取番剧信息
response_data = crawl_bilibili_saisi()   #获取B站赛事信息
if response_data:
    print(response_data)
    save_json_to_file(response_data, "json/bilibili_data.json")
else:
    print("Failed to fetch data.")
