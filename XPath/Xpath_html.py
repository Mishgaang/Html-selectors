import requests
from urllib.request import urlopen
from lxml import etree

# get html from site and write to local file
url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
headers = {'Content-Type': 'text/html', }
response = requests.get(url, headers=headers)
html = response.text
with open('star_wars_html', 'w') as f:
    f.write(html)

# read local html file and set up lxml html parser
local = 'file:///home/user/PycharmProjects/HTML_proj/XPath/star_wars_html'
response = urlopen(local)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)


def parser():
    name = tree.xpath('//p/strong[not(contains(text(),"\xa0"))]/text()')  # Запрос с фильтрацией нежелательного контента
    print(name)
    text = tree.xpath('//p[contains(text(),"Use")]/text()')     # Фильтрация для получения контента по ключевому слову
    print(text)
    img = tree.xpath('//img[starts-with(@class, "alignnone")]/@src')    # Получение узлов, которые начинаются с ключевого слова
    print(img)
    all_info = tree.xpath('//header[@class="article-header"]/descendant::node()/text()')     # Получение узлов на основе отношений
    print(all_info)
    href = tree.xpath('//li[@class="related-post"]/a[1]/@href')    # Получение узлов на основе индекса
    print(href)


parser()
