
# coding:utf-8

# 从lol电影天堂搜索功能  idx===>关键字

import urllib2
import time
from bs4 import BeautifulSoup
from SqlOperation import OperSql


class UrlList():
    # 迅雷搜索的链接
    templateUrl = "http://www.loldyttw.net/e/search/result/?searchid=%s"

    # url链接信息列表
    urls = []

    # 是否还有未抓取的链接
    hasUrl = True

    def __init__(self, startIdx, endIdx):
        for idx in range(startIdx, endIdx):
            self.urls.append(self.__generateUrl__(idx))

    # 根据idx返回可用的url信息
    def __generateUrl__(self, idx):
        return {"url": self.templateUrl % (idx), "idx": idx}

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


class DataParser():
    # 解析迅雷搜索结果页面的数据
    def __init__(self, htmlDom,  searchId):
        self.htmlDom = htmlDom
        self.searchId = searchId

    def parser(self):

        # searchId
        # keywords
        # moviesUrlList

        keyWord = self.htmlDom.select('.solb b')[0].get_text()
        parsedData = {
            'keyWord': keyWord,
            'searchId': self.searchId
        }

        return parsedData


operTablePython = OperSql('python')
# 失败的链接
failIdx = []
# for urlInfo in UrlList().getUrls():
URLLIST = UrlList(2000, 4000)
while(URLLIST.hasUrl):
    urlInfo = URLLIST.getUrl()
    urlIdx = urlInfo['idx']
    urlAddress = urlInfo['url']
    print urlAddress
    try:
        res = urllib2.urlopen(urlAddress)
        if(res.code == 200):
            htmlDom = BeautifulSoup(
                res.read(), 'html.parser', from_encoding='gb2312')
            data = DataParser(htmlDom, urlIdx).parser()
            operTablePython.oper(lambda conn, cursor: cursor.execute(
                "insert into test (idx,keyword) values ('%s','%s')" % tuple(data.values()))
            )
            operTablePython.oper(lambda conn, cursor: conn.commit())
            print urlAddress + ' ---- Collect the data successfully'

        else:
            print urlAddress + ' ---- Connection failed'
            continue
    except Exception as identifier:
        print(identifier)
        print(urlIdx)
        # 添加失败的链接
        URLLIST.addFailUrl(urlIdx)
        print(URLLIST.urls)
        time.sleep(2)
        continue

operTablePython.close()
