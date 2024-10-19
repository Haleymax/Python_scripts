import re


singer_page_regex = re.compile(r'<ul class="mul" style="background:#fff;overflow:hidden;">(?P<ul>.*?)</ul>', re.S)
song_url_regex = re.compile(r'<ul class="mul" style="background:#fff;overflow:hidden;">(?P<ul>.*?)</ul>', re.S)
music_page_url_regex = re.compile(r'<label class="layui-form-label">MP3地址</label>.*?<input type="text" value=(?P<link>.*?)name="vercode"')
input_pattern_regex = re.compile(r'<input type="text" value="([^"]+)" name="vercode"')
