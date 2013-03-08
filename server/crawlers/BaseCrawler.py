#coding: utf-8

import urllib
import urllib2

class BaseCrawler:
    def __init__(self, base_url, params=None):
        self.base_url = base_url;
        self.params = params;

    def run(self):
        if self.params:
            for param in self.params:
                self.crawl(self.base_url + "?" + urllib.urlencode(param));
                self.exec_scraping();
        else:
            self.crawl(self.base_url);
            self.exec_scraping();

    def crawl(self, url):
        f = urllib2.urlopen(url);
        self.source = f.read();

    def exec_scraping(self):
        import bs4
        self.pre_scraping(self.source);
        bs = bs4.BeautifulSoup(self.source);
        self.scraping(bs);

    #スクレイピングの前の文書整形
    def pre_scraping(self, html):
        pass;
    
    #スクレイピングを行う
    def scraping(self, bs):
        pass;

if __name__ == "__main__":
    pass;

