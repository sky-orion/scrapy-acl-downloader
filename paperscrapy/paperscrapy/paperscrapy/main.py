from scrapy import cmdline


#执行命令行 修改年份就行了 改完年份还得改pipline文件里存储年份！！！
cmdline.execute('scrapy crawl acl  -a event=acl -a year=2020 '.split())
#也可以在命令行输入上面语句
#还得改piplines文件里的年份！！！