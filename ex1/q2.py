from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
import requests
from lxml import etree
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.ucas.ac.cn/'
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36 "
    }
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')

    html = etree.HTML(content)
    ul_1 = html.xpath('/html/body/header/div[4]/nav/ul')
    for ul in ul_1:
        li = ul.xpath('./li')
        for li_item in li:
            title = li_item.xpath('./a/text()')
            print(title[0])
            sub_dl = li_item.xpath('./div/dl')
            for sub in sub_dl:
                print('\t'+'\n\t'.join(sub.xpath('.//a/text()')))
