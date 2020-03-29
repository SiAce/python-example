from lxml import etree

parser = etree.HTMLParser()
tree   = etree.parse("app.html", parser)

name_xpath_1 = '/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[2]/div[2]/div/div[3]/text()'
name_xpath_2 = '/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[1]/div[2]/div/div[3]/text()'

name_1 = tree.xpath(name_xpath_1)
name_2 = tree.xpath(name_xpath_2)

print(name_1)
print(type(name_1))
print(name_2)
print(type(name_2))

