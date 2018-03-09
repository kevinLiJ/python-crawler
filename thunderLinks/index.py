# coding:utf-8
import urllib2
from bs4 import BeautifulSoup

from dataParser import DataParser
from urlManagement import UrlManagement
from SqlOperation import OperSql

# movieTypes = ['Dongzuopian', 'Kehuanpian', 'Kongbupian', 'Xijupian', 'Aiqingpian',
#               'Juqingpian', 'Zhanzhengpian', 'Dongman', 'Zongyi']
movieTypes = ['Aiqingpian',
              'Juqingpian', 'Zhanzhengpian', 'Dongman', 'Zongyi']
# 操作movie_info表
sqlMovieInfo = OperSql('python')
for movieType in movieTypes:
    # 电影的链接
    URLS = UrlManagement(movieType, 1000, 10000)

    # 查询已有的idx，爬取数据时跳过
    existedIdx = []
    sqlMovieInfo.oper(
        lambda conn, cursor: cursor.execute("select page_idx from movie_info"))
    result = sqlMovieInfo.oper(
        lambda conn, cursor: cursor.fetchall())
    for UIdx in result:
        existedIdx.append(UIdx[0])

    # 循环链接并尝试爬取数据
    while(URLS.hasUrl):
        urlInfo = URLS.getUrl()
        urlLink = urlInfo['url']
        urlIdx = urlInfo['idx']
        # 跳过已存在idx
        if(urlIdx in existedIdx):
            print("  ---skip" + str(urlIdx))
            continue

        # 尝试爬取链接数据
        try:
            print(urlLink + ' - --begin')
            res = urllib2.urlopen(urlLink)
            if(res.code == 200):
                # 解析数据
                # 实践中，lxml解析数据不会乱码
                htmlDom = BeautifulSoup(
                    res.read(), 'lxml', from_encoding='utf-8')
                movieInfo = DataParser(movieType, htmlDom, urlIdx).parser()
                # 可能会出现没有解析到数据的情况，具体原因未知
                if(movieInfo == None):
                    continue
                # 存储数据库
                sqlMovieInfo.oper(lambda conn, cursor: cursor.execute(
                    "insert into movie_info(page_idx, movie_name, type, poster_href, lead_actor, thunder_links, bt_links) \
                    values \
                    ('%(pageIdx)d', '%(movieName)s', '%(type)s', '%(posterHref)s', '%(leadActor)s', '%(thunderLinks)s', '%(btLinks)s')" % movieInfo)
                )
                sqlMovieInfo.oper(lambda conn, cursor: conn.commit())

                print(urlLink + '  ---success')
        except Exception as e:
            print(e)
            print(urlLink + '  ---fail')
            if('404' not in str(e)):
                # 地址存在但连接失败的链接，重新添加进队列
                URLS.addFailUrl(urlIdx)

sqlMovieInfo.close()
