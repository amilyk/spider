# spider
#### 简介

​	python爬取百度百科前1000个python相关页面  ——学自慕课网

#### 说明

​	需要新建一个python package，名为spider。也可在spider_main.py中修改，from后的名称就是新建package的名称。

```python
from spider import url_manager, html_downloader, html_parser, html_outputer
```

​	整个爬虫程序分为：

+ spider_main.py 调度器，管理整个爬虫的运行。
+ url_manager.py URL管理器，添加新URL、获取待爬取URL
+ html_downloader.py 网页下载器，将网页以html的形式下载到本地
+ html_parser.py 网页解析器，将下载器获得的字符串解析。一方面得到有价值的数据，另一方面得到新的URL补充新URL列表
+ html_outputer.py 网页输出器，将获取的数据以html形式展现。其结果保存在当前目录下的output.hmtl中。