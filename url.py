# coding:utf-8
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
from data_parser import DataParser
from url_magager import UrlManager
doubanData = []
# 循环url管理器的url列表，解析网页
for url in UrlManager().urlList():
    # 使用urllib2连接网页
    res = urllib2.urlopen(url)
    if res.code == 200:
        # 使用BeautifulSoup解析网页
        htmlDom = BeautifulSoup(
            res.read(), 'html.parser', from_encoding='utf-8')

        # 使用class DataParser收集网页中的数据
        parsedData = DataParser(htmlDom).parser()

        # 如果没有数据，则解析下一个url
        if (len(parsedData) == 0):
            print url + ' ---- This URL has no data'
            continue

        # 拼接解析的数据
        doubanData = doubanData + parsedData
        print url + ' ---- Collect the data successfully'
    else:
        print url + ' ---- Connection failed'

douban = open('doubanData.txt', 'a+')
for item in doubanData:
    douban.write(item)
