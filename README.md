# scrapy-acldownloader
利用scrapy 爬虫框架 下载ACL会议论文 
#1.安装scrapy 
#2.运行 main.py 需要修改文件中的年份 
也可以进入项目目录 打开命令行 输入 scrapy crawl acl  -a event=acl -a year=2020 爬取2020年的acl论文
#3.pipelines 文件最上面修改年份 默认保存D:/result/xxxx xxxx是修改的年份值
pipelines 与main文件中的年份要保存一致 确保抓取论文放在一个文件夹里
#4.从1979年 到2020年 的acl，emnlp taacl naacl文章都能下载下来
