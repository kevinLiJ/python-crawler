# coding:utf-8
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
from data_parser import DataParser
from url_magager import UrlManager
doubanData = []
for url in UrlManager().urlList():
    print url
    res = urllib2.urlopen(url)
    htmlDom = BeautifulSoup(res.read(), 'html.parser', from_encoding='utf-8')
    doubanData = doubanData + DataParser(htmlDom).parser()

douban = open('doubanData.txt', 'a+')
for item in doubanData:
    douban.write(item)
