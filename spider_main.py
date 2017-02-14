# -*- coding: utf-8 -*-
##加utf格式就能支持中文注释
#调度器

# 入口URL作为参数爬取页面
from spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):  # 创建类快捷键ctrl+1
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # url下载器
        self.parser = html_parser.HtmlParser()  # url解析器
        self.outputer = html_outputer.HtmlOutputer()  # html输出器

    def craw(self, root_url):  # 入口url添加进管理器
        cnt = 1
        self.urls.add_new_url(root_url)  # 当url管理器有待爬取的url，启动循环
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 获取一个待爬取的
                print 'craw %d: %s' % (cnt, new_url)  ##爬取的为第几个url
                html_cont = self.downloader.download(new_url)  # url下载器
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 当前爬取的新url，解析后的价值数据
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if cnt == 3: ##爬取1000个页面就停止，可以自行调整
                    break
                cnt = cnt + 1

            except: #有些页面没有简介
                print 'craw failed'

        self.outputer.output_html() #结果保存在当前目录下output.html中


if __name__ == "__main__":
    # python词条 入口URL
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
