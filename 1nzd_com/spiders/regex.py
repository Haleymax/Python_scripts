import re


singer_page_regex = re.compile(r'<ul class="mul" style="background:#fff;overflow:hidden;">(?P<ul>.*?)</ul>', re.S)
song_url_regex =re.compile(r"<a href='(?P<href>[^']+)' target='_blank' title=''><font color='red'>周杰伦</font>/(?P<name>[^<]+)</a></li>", re.IGNORECASE)
