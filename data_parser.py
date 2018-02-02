class DataParser():

    def __init__(self, htmlDom):
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

        return parsedData
