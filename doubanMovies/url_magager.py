# coding:utf-8
class UrlManager():
    # 豆瓣高分电影地址

    urlTemplate = 'https://www.douban.com/doulist/240962/?start=%s&sort=seq&sub_type='

    def urlList(self):
        urlList = []
        for i in range(0, 12):
            if i == 0:
                url = 'https://www.douban.com/doulist/240962'
            else:
                url = self.urlTemplate % (25 * i)
            urlList.append(url)
        return urlList


if __name__ == '__main__':
    urlList = UrlManager().urlList()
    print urlList
