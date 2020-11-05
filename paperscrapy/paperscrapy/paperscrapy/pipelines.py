# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# 只需修改年份！！！
year = 2018 #年份修改
conference = "acl"
from itemadapter import ItemAdapter
import scrapy
import re
from scrapy.pipelines.files import FilesPipeline
from paperscrapy.spiders.acl import  AclSpider
class PaperscrapyPipeline:
    def process_item(self, item, spider):
        with open(r"D:\result\paper-%s-short-%d.txt" %( conference, year),'a') as fp:#把下载的论文放入txt中
            fp.write(item['name']+'\n')
        return item

class DownloadPapersPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for paper_url in item['url']:
            yield scrapy.Request(paper_url,meta={'item': item['name']})
    def file_path(self, request, response=None, info=None):
        paper_name = request.meta['item']
        paper_name = re.sub("[\*:\?<>\|/\\\"]+",'',str(paper_name))#防止写文件时出现错误
        #re是正则的表达式,sub是substitute表示替换
        return '%s/%dshort/%s.pdf' % (conference, year, paper_name)#这里得加一个阔号
