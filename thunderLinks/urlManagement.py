# coding:utf-8
class UrlManagement():
    # 用于输出lol电影天堂电影的页面链接

    # 类型['Dongzuopian','Kehuanpian','Kongbupian','Xijupian','Aiqingpian',
    #       'Juqingpian','Zhanzhengpian','Dongman','Zongyi'...]

    templateUrl = "http://www.loldyttw.net/%s/%d.html"

    # url链接信息列表
    urls = []

    # 是否还有未抓取的链接
    hasUrl = True

    # 电影类型
    type = ''

    def __init__(self, type, startIdx,  endIdx):
        self.type = type
        for idx in range(startIdx, endIdx):
            self.urls.append(self.__generateUrl__(idx))

    # 根据idx返回可用的url信息
    def __generateUrl__(self, idx):
        return {"url": self.templateUrl % (self.type, idx), "idx": idx}

    # 添加数据抓取失败的链接,用以重新抓取
    def addFailUrl(self, idx):
        self.urls.append(self.__generateUrl__(idx))
        self.hasUrl = True

    # 获取url列表的接口
    def getUrl(self):
        if (len(self.urls) > 0):
            currentUrl = self.urls[0]
            del self.urls[0]
            if (len(self.urls) == 0):
                self.hasUrl = False
            return currentUrl
        else:
            return False


if (__name__ == "__main__"):
    URLS = UrlManagement('dongzuopian', 1, 100)
    while(URLS.hasUrl):
        print URLS.getUrl()['url']
