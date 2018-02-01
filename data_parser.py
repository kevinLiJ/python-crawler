import chardet
import io

class DataParser():
    
    def __init__(self,htmlDom):
        self.htmlDom = htmlDom

    def parser(self):
        parsedData = []
        for itemDom in self.htmlDom.select('.doulist-item'):
            
            aDom = itemDom.select('.title a')
            if len(aDom) == 0:
                continue
            title = itemDom.select('.title a')[0].get_text()
            score = itemDom.select('.rating .rating_nums')[0].get_text()
            parsedData.append(title + score)
            # print title
            # print title + score
            # print '\u8096\u7533\u514b\u7684\u6551\u8d4e'
            # print type(title)
            # print parsedData
            # break
            

        return parsedData
        # return str(parsedData).decode('unicode_escape').replace('u"','')
        