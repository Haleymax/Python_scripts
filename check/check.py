import re
from datetime import datetime

def extract_time(log_line, keyword):
    """
    从日志行中提取耗时信息（单位：毫秒）。
    """
    match = re.search(rf"{keyword}:\s*([\d.]+)\s*(ms|s)", log_line)
    if match:
        value, unit = match.groups()
        value = float(value)
        if unit == "s":
            value *= 1000
        return int(value)
    return None

def extract_timestamp(log_line, keyword):
    """
    从日志行中提取时间戳。
    """
    match = re.search(rf"{keyword}：\s*(\d{{4}}-\d{{2}}-\d{{2}}T\d{{2}}:\d{{2}}:\d{{2}}\.\d{{3}}Z)", log_line)
    if match:
        return match.group(1)
    return None

def calculate_time_difference(start_time_str, end_time_str):
    """
    计算两个时间戳之间的差值（毫秒）。
    """
    if not start_time_str or not end_time_str:
        return 0  # 如果时间戳为 None，返回 0

    format_str = "%Y-%m-%dT%H:%M:%S.%fZ"  # 适配时间戳格式
    start_time = datetime.strptime(start_time_str, format_str)
    end_time = datetime.strptime(end_time_str, format_str)
    time_diff = (end_time - start_time).total_seconds() * 1000  # 转换为毫秒
    return int(time_diff)

def parse_log_line(line):
    """
    解析单行日志，提取耗时信息。
    """
    resource_download_time = extract_time(line, "下载资源包耗时")
    resource_unzip_time = extract_time(line, "解压资源包耗时")
    wasm_download_time = extract_time(line, "下载wasm代码包")
    callmain_time = extract_time(line, "callMain耗时")
    game_start_time = extract_time(line, "游戏启动耗时")
    subwasm_compile_time = extract_time(line, "subwasm编译耗时")
    wasm_compile_time = extract_time(line, "wasm编译耗时")

    # 提取时间戳
    start_download_subwasm_time = extract_timestamp(line, "开始下载 WASM 分包")
    end_download_subwasm_time = extract_timestamp(line, "下载 WASM 分包完成")
    start_compile_wasm_time = extract_timestamp(line, "开始编译 WASM 首包")
    end_compile_wasm_time = extract_timestamp(line, "编译 WASM 首包完成")
    start_compile_subwasm_time = extract_timestamp(line, "开始编译 WASM 分包")
    end_compile_subwasm_time = extract_timestamp(line, "编译 WASM 分包完成")

    return {
        "resource_download_time": resource_download_time,
        "resource_unzip_time": resource_unzip_time,
        "wasm_download_time": wasm_download_time,
        "callmain_time": callmain_time,
        "game_start_time": game_start_time,
        "subwasm_compile_time": subwasm_compile_time,
        "wasm_compile_time": wasm_compile_time,
        "start_download_subwasm_time": start_download_subwasm_time,
        "end_download_subwasm_time": end_download_subwasm_time,
        "start_compile_wasm_time": start_compile_wasm_time,
        "end_compile_wasm_time": end_compile_wasm_time,
        "start_compile_subwasm_time": start_compile_subwasm_time,
        "end_compile_subwasm_time": end_compile_subwasm_time,
    }

def parse_log_file(file_path):
    """
    解析日志文件，提取并计算耗时信息。
    """
    resource_download_time = 0
    resource_unzip_time = 0
    wasm_download_time = 0
    callmain_time = 0
    game_start_time = 0
    subwasm_compile_time = 0
    wasm_compile_time = 0
    start_download_subwasm_time = None
    end_download_subwasm_time = None
    start_compile_wasm_time = None
    end_compile_wasm_time = None
    start_compile_subwasm_time = None
    end_compile_subwasm_time = None

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                result = parse_log_line(line)
                if result["resource_download_time"]:
                    resource_download_time = result["resource_download_time"]
                if result["resource_unzip_time"]:
                    resource_unzip_time = result["resource_unzip_time"]
                if result["wasm_download_time"]:
                    wasm_download_time = result["wasm_download_time"]
                if result["callmain_time"]:
                    callmain_time = result["callmain_time"]
                if result["game_start_time"]:
                    game_start_time = result["game_start_time"]
                if result["subwasm_compile_time"]:
                    subwasm_compile_time = result["subwasm_compile_time"]
                if result["wasm_compile_time"]:
                    wasm_compile_time = result["wasm_compile_time"]

                # 提取时间戳
                if result["start_download_subwasm_time"]:
                    start_download_subwasm_time = result["start_download_subwasm_time"]
                if result["end_download_subwasm_time"]:
                    end_download_subwasm_time = result["end_download_subwasm_time"]
                if result["start_compile_wasm_time"]:
                    start_compile_wasm_time = result["start_compile_wasm_time"]
                if result["end_compile_wasm_time"]:
                    end_compile_wasm_time = result["end_compile_wasm_time"]
                if result["start_compile_subwasm_time"]:
                    start_compile_subwasm_time = result["start_compile_subwasm_time"]
                if result["end_compile_subwasm_time"]:
                    end_compile_subwasm_time = result["end_compile_subwasm_time"]

        # 计算 WASM 分包下载耗时
        subwasm_download_time = calculate_time_difference(start_download_subwasm_time, end_download_subwasm_time)

        # 计算 WASM 首包编译耗时
        wasm_compile_time = calculate_time_difference(start_compile_wasm_time, end_compile_wasm_time)

        # 计算 WASM 分包编译耗时
        subwasm_compile_time = calculate_time_difference(start_compile_subwasm_time, end_compile_subwasm_time)

        # 输出结果
        print(f"资源包下载耗时: {resource_download_time}ms")
        print(f"资源包解压耗时: {resource_unzip_time}ms")
        print(f"WASM 首包下载耗时: {wasm_download_time}ms")
        print(f"WASM 分包下载耗时: {subwasm_download_time}ms")
        print(f"WASM 首包编译耗时: {wasm_compile_time}ms")
        print(f"WASM 分包编译耗时: {subwasm_compile_time}ms")
        # print(f"wasm 编译耗时: {wasm_compile_time}ms")
        print(f"CALLMAIN 耗时: {callmain_time}ms")
        print(f"游戏启动耗时: {game_start_time}ms")

    except FileNotFoundError:
        print(f"文件 {file_path} 未找到")
    except Exception as e:
        print(f"解析日志文件时发生错误: {e}")

if __name__ == "__main__":
    print("sdk 1.1.0")
    split = "123"
    game = "zhuxian"
    pack = "Terrible"
    for i in range(1, 6):
        print(f"第 {i} 轮结果")
        log_file_path = r"D:\project\python\Python_scripts\check\{}\{}\{}\110_{}.txt".format(split, game, pack, i)
        parse_log_file(log_file_path)
        print("----------------------------------------------------------------------------------------------------------")

    # log_file_path2 = r"D:\project\python\Python_scripts\check\122\dadao\Normal\110_3.txt"
    # parse_log_file(log_file_path2)