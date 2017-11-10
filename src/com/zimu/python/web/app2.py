
class QsbkClassCrawler:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent':self.user_agent}
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构建请求的request
            request = urllib.request.Request(url, headers = self.headers)
            # 利用urlopen获取页面代码
            response = urllob.request.urlopen(request)
            # 将页面转化为UTF-8编码
            pageCode = response.read.decode('utf-8')
            return pageCode
        except urllib.request.URLError as e:
            if hasattr(e, "reason"):
                print("连接糗事百科失败,错误原因", e.reason)
                return None

    # 传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print("页面加载失败...")
            return None
        pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>',
                             re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(), item[2].strip()])
        return pageStories


