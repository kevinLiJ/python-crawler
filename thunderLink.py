# coding:utf-8
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

movieName = '拼命三郎石秀'


class UrlList():

    templateUrl = "http://www.loldyttw.net/e/search/result/?searchid=%s"

    urls = []

    def getUrls(self):
        if(len(self.urls) != 0):
            return self.urls

        for idx in range(2000, 2020):
            url = self.templateUrl % (idx)
            self.urls.append({'url': url, 'idx': idx})
        return self.urls


class DataParser():

    def __init__(self, htmlDom, searchId):
        self.htmlDom = htmlDom
        self.searchId = searchId

    def parser(self):

        # searchId
        # keywords
        # moviesUrlList

        parsedData = []

        keyWord = self.htmlDom.select('.solb b')[0].get_text()
        parsedData.append({
            'keyWord': keyWord,
            'searchId': self.searchId
        })
        # for itemDom in self.htmlDom.select('.doulist-item'):
        #     aDom = itemDom.select('.title a')
        #     if len(aDom) == 0:
        #         continue
        #     title = itemDom.select('.title a')[0].get_text()
        #     score = itemDom.select('.rating .rating_nums')[0].get_text()
        #     parsedData.append(title + score)

        return parsedData


doubanData = []
for urlInfo in UrlList().getUrls():
    print urlInfo['url']
    res = urllib2.urlopen(urlInfo['url'])
    htmlDom = BeautifulSoup(res.read(), 'html.parser', from_encoding='utf-8')
    doubanData = doubanData + DataParser(htmlDom, urlInfo['idx']).parser()
    # print urlInfo.url

print doubanData
# douban = open('doubanData.txt', 'a+')
for item in doubanData:
    # douban.write(item)
    print item['keyWord']
