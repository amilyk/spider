# -*- coding: utf-8 -*-
#URL管理器

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

     # 添加单个url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)  ##新的url

    # 添加一批url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #在url管理器中获取待爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    #管理器中是否有待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

