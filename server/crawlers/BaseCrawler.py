#coding: utf-8

import urllib
import urllib2
import pymongo

class BaseCrawler:
    COLLECTION = None;
    METHOD = "GET";

    def __init__(self, base_url, params=None):
        self.base_url = base_url;
        self.params = params;

    def run(self, *args, **kwargs):
        self.args = args;
        
        self.pre_crawling();
        self.crawl(self.base_url, self.METHOD);
        res = self.exec_scraping();

        if self.COLLECTION:
            db = pymongo.Connection()[self.COLLECTION];
        else:
            db = None
        self.save(res, db);

    def crawl(self, url, method):
        if (method == "GET"):
            f = urllib2.urlopen(url);
        else:
            f = urllib2.urlopen(url, urllib.urlencode(self.params));
        self.source = f.read();

    def exec_scraping(self):
        import bs4
        self.pre_scraping(self.source);
        bs = bs4.BeautifulSoup(self.source);
        res = self.scraping(bs);
        return res

    def pre_crawling(self):
        pass
    #スクレイピングの前の文書整形
    def pre_scraping(self, html):
        pass;
    
    #スクレイピングを行う
    def scraping(self, bs):
        pass;

    def save(self, result, db):
        pass
if __name__ == "__main__":
    pass;

