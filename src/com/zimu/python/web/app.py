# -*- coding:utf-8 -*-
import urllib.request
import urllib.error
import re
import time

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(1)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-agent': user_agent}
count = 0
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    time.sleep(2)
    pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern,content)

    for item in items:
        print("Author" + item[0])
        print("Content:" + item[1])
        print("favourite" + item[2])
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.reason)
else:
    print("Executed!")