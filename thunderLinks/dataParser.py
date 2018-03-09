# coding:utf-8


class DataParser():
    # 解析迅雷电影详情页面的数据
    def __init__(self, movieType, htmlDom,  pageIdx):
        self.htmlDom = htmlDom
        self.pageIdx = pageIdx
        self.type = str(movieType)

    def parser(self):

        # pageIdx
        # movieName 电影名称
        # movieType 电影类型
        # posterHref 海报图片链接
        # leadActor 主演
        # thunderLinks 迅雷链接
        # btLinks bt链接
        if(len(self.htmlDom.select('body')) == 0):
            return None
        movieName = self.htmlDom.select('center .lm a')[0].get_text()
        print(movieName)
        posterHref = self.htmlDom.select('center .haibao a img')[0]['src']
        leadActor = self.htmlDom.select('center .zhuyan ul li')[0].get_text()

        thunderLinks = ''
        btLinks = ''
        if(len(self.htmlDom.select('center .downurl')) != 0):
            thunderLinks = self.htmlDom.select('center .downurl a')

        if(len(self.htmlDom.select('center #bt')) != 0):
            btLinks = self.htmlDom.select('center #bt a')

        parsedData = {
            "pageIdx": self.pageIdx,
            'movieName': movieName,
            "type": self.type,
            "posterHref": posterHref,
            "leadActor": leadActor,
            "thunderLinks": thunderLinks,
            "btLinks": btLinks
        }

        return parsedData


if (__name__ == "__main__"):
    if(None):
        print('--------------')

    import urllib2
    from bs4 import BeautifulSoup
    from bs4.diagnose import diagnose
    res = urllib2.urlopen('http://www.loldyttw.net/Dongman/954.html')
    if(res.code == 200):
        htmlDom = BeautifulSoup(
            res.read(), 'lxml', from_encoding='utf-8')
        data = DataParser('喜剧', htmlDom, 25317).parser()
        diagnose(res.read())
        print(data['movieName'])
