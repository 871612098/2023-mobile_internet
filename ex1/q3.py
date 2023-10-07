"""

3、从人民网（http://cpc.people.com.cn/GB/87228/index1.html）上抓取24小时滚动新闻：
     要求完成的：文章的标题、链接，并且支持多页爬取

"""

import urllib.request
import re
import requests
from bs4 import BeautifulSoup
def visit(url):

    headers = {
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/116.0.0.0 Safari/537.36 "
    }
    response = requests.get(url,headers = headers)
    # 网页代码gb2312
    response.encoding = 'gb2312'
    content = response.text
    soup = BeautifulSoup(content)
    for ul_index, ul_item in enumerate(soup.select(".fl > ul > li")):
        link = ul_item.a.attrs['href']
        title = ul_item.a.text
        if len(re.findall("http://.*?", link)) == 0:
            link = 'http://cpc.people.com.cn/' + link
        print(link, title)

if __name__ == '__main__':
    pages  = eval(input("请输入你想爬取的页数：（最大不超过7页）"))
    for i in range(1,pages+1):
        print("正在爬取第"+str(i)+"页：")
        url = 'http://cpc.people.com.cn/GB/87228/index'+str(i)+'.html'
        visit(url)
    print("爬取结束！")





