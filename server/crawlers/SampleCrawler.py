#coding: utf-8

from BaseCrawler import BaseCrawler

class SampleCrawler(BaseCrawler):
    def pre_scraping(self, html):
        pass;

    def scraping(self, bs):
        print bs.find("title").text;

if __name__ == '__main__':
    sample = SampleCrawler("http://google.com");
    sample.run();

