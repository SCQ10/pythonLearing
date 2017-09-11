# coding=utf-8
from baike_spider import html_downloader, url_manager, html_parser,\
    html_outputer
import time


class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDowmloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s ' % (count, new_url))
                html_doc = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_doc)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 100:
                    break
            except:
                print('craw failed')
            count += 1
        self.outputer.output_html()



if __name__ == '__main__':
    time1 = time.time()
    root_url = 'https://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    time2 = time.time()
    print('一共跑了 %s s' % int(time2 - time1))