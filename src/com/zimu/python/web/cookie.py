import urllib
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print ('Name = '+item.name)
    print ('Value = '+item.value)
#利用cookie请求访问另一个网址
gradeUrl = 'http://www.baidu.com/xxx/xx'
#请求访问
result = opener.open(gradeUrl)
print (result.read())