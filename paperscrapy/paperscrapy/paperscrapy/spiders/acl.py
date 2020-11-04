import scrapy
import string
from itertools import chain

from paperscrapy.items import PaperscrapyItem
class AclSpider(scrapy.Spider):
    name = 'acl'
    allowed_domains = ['aclweb.org']

    # start_urls = ['https://www.aclweb.org/anthology/events/acl-2020/#2020-acl-main']
    def __init__(self, event="acl", year="2020", *args, **kwargs):
        super(AclSpider, self).__init__(*args, **kwargs)
        self.event = event
        self.year = int(year)#给类传参数
        self.start_urls = ["https://www.aclweb.org/anthology/events/%s-%d" % (event, int(year))]

    def parse(self,response):
        if self.event == "acl" and int(self.year) >= 2020:
            Papers = response.xpath("//*[@id='%d-acl-main']/p" % int(self.year))  # 复制xpath就行了，把双引号改成单引号
        elif self.event == "acl" and 2019 >= int(self.year) >= 2010:
            Papers = response.xpath("//*[@id='p%d-1']/p" % (int(self.year)-2000))
        elif self.event == "acl" and 2010 > int(self.year) >= 2000:
            Papers = response.xpath("//*[@id='p0%d-1']/p" % (int(self.year)-2000))
        elif self.event == "acl" and int(self.year) <= 2000:
            Papers = response.xpath("//*[@id='p%d-1']/p" % (int(self.year)-1900))
        # elif self.event == "acl" and self.year == "2018":
        #     Papers = response.xpath("//*[@id='p18-1']/p")

        for papers in Papers:
                item = PaperscrapyItem()
                a = papers.xpath("./span[2]/strong/a/span/text()").getall()[:]
                b = papers.xpath("./span[2]/strong/a/text()").getall()[:]
                if len(a) <= len(b):
                    while len(b) != len(a):
                        a.extend(' ')
                elif len(a) > len(b):
                    while len(b) != len(a):
                        b.extend(' ')
                item['name'] = "".join(list(chain.from_iterable(zip(a, b))))#谜之网页代码 必须这样才能把标题全部提取
                item['url'] = [papers.xpath("./span[1]/a[1]/@href").get()]
                yield item

