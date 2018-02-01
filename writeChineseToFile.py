import codecs  
test = codecs.open('chineseTest.txt','wb','utf-8')
name = unicode.decode
test.write(u'李阳')