#coding: utf-8

from BaseCrawler import BaseCrawler

class CharactorImageCrawler(BaseCrawler):
    METHOD = "GET"
    COLLECTION = "kawaii"

    def scraping(self, bs):
        images_wrap = bs.find(attrs={"class": "MdImgList01"});
        return [img.attrs["src"] for img in images_wrap.find_all("img")];

    def save(self, result, db):
        id = self.args[0];
        button = db.buttons.find_one({"_id": id});
        button["images"] = result;
        db.buttons.save(button);

