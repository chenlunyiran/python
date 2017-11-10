# -*- coding:utf-8 -*-
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(1)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-agnet': user_agent}
count = 0
try:
    request = urllib.request.Request(url, headers = headers)