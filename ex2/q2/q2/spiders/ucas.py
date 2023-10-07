import scrapy

from ex2.q2.q2.items import Q2Item

count = 1
class UcasSpider(scrapy.Spider):
    name = "ucas"
    # allowed_domains = ["old-www.ucas.ac.cn"]
    # start_urls = ["http://old-www.ucas.ac.cn/"]
    #  allowed_domains = ["https://old-www.ucas.ac.cn/site/263"]
    start_urls = ["https://old-www.ucas.ac.cn/site/263"]

    def parse(self, response):
        mix = response.xpath('/html/body/div[4]/div[2]/div[2]/div[3]//p')
        for item in mix:
            title = item.xpath('./a/text()').get()
            link = item.xpath('./a/@href').get()
            time = item.xpath('./span/text()').get()
            print(link,title,time)
            item = Q2Item(title = title,link=link,time = time)
            yield item
        ## 获取下一页url
        global count
        count += 1
        # next_url = response.xpath("/html/body/div[4]/div[2]/div[2]/div[4]/span/a/@href").extract_first()  # 找到按钮'下一页'的href
        if count <= 30:
            url = 'https://old-www.ucas.ac.cn/site/263?pn='+ str(count)
            # print(url)
            yield scrapy.Request(url, callback=self.parse)


