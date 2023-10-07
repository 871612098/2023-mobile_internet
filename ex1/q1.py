

"""
1、URILIB+正则表达式
     Ucas网站四个校区的名称、地址、邮编和电话号码的爬取

"""
# import urllib.request
# import requests
# from bs4 import BeautifulSoup
# import re
# from lxml import etree
# if __name__ == '__main__':
#     url = 'https://www.ucas.ac.cn/'
#     headers = {
#         'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/116.0.0.0 Safari/537.36 "
#     }
#     response = urllib.request.urlopen(url)
#     content = response.read().decode('utf-8')
#     # soup = BeautifulSoup(content)
#     # for item in soup.select('.box'):
#     #     print(item.get_text())
#     # address = '.*校区'
#     # con = re.compile(address)
#     # res = con.findall(content)
#     # print(res)
#     html = etree.HTML(content)
#     path = html.xpath('/html/body/div[3]/div[11]/div[2]/footer/div[1]/div[1]/div')
#     for item in path:
#         print(item.xpath('./div/div[1]/text()'))
#         print(item.xpath('./div/div/p/text()'))
#
#
import urllib.request
import re

url = "https://www.ucas.ac.cn/"
flag = 0
count = 0
with urllib.request.urlopen(url) as response:
    for line in response:
        line = line.decode('utf-8')
        if flag == 0:   # 寻找校区名
            result = re.search('(?<=<div class="title fs18">).*?(?=</div>)', line)
            if result != None:  # 找到校区名
                print(result.group())
                flag = 1
        elif flag == 1:   #寻找校区详细信息
            result = re.search('(?<=<p>).*?(?=</p>)', line)
            if result != None:  # 找到校区名
                print(result.group())
                count += 1
                if count == 3:
                    flag = 0
                    count = 0