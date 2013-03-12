#coding: utf-8

from BaseCrawler import BaseCrawler
import urllib

IMAGE_BASE = "/Users/yuta/kawaiibutton/static/img/";

URL = "http://www.simwebsol.com/imagetool/default.aspx"
PARAMS = {
        "__VIEWSTATE":"/wEPDwUKMTkyNTg4NjcxNGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgQFDENoZWNrQm94Qm9sZAUOQ2hlY2tCb3hJdGFsaWMFEUNoZWNrQm94VW5kZXJsaW5lBQ5DaGVja0JveE1pcnJvcg18rZ9rSGcraW/bvvBz4HOk165Y",
        "__EVENTVALIDATION":"/wEWQgL//9fYBwKIrpbVCwKk18beAgLDmcTeBwLBxpmqCQKA1PDuCQKj5Z/MBwKg5Z/MBwKPnbCmCwKYlrLYCgLCptDWCQKJkoXaAgL2tPoNAo7Lz8MDAsXUvfUFAsbUvfUFAsbUgfUFAsfUvfUFAsDUvfUFAsHUvfUFAsLUvfUFAtPUvfUFAuPs2OcLAp71uv0NArXelIoHAoC01MsPAr+dtuEBAvv+5/0OAp6aycQIAo3c+c0CArbN6DwCrpHy4wECv/Cs0QICvrb1jQgC053eiAQCnJm09AkC0c2DvQcC2JO5jw0C1OXN6gsC1fPT7AwCurDI+g4C87mFgwgC8cuS3QcC1OPW5wgCzZeeWALFnd0qArffxMoEAsOUgOgFAtnHsp4DAuOlkLEPArzG/oYGArrm7b0LAsnsxuEGAsjsxuEGAsaD7I8KAoS35PQBApq31PQBAqT2/6AGAqr2i6MGAqn2i6MGArz2i6MGAqT2w54NAtfr1uUEAqWAyNIKAs3rjuQEAsO0jM4BsnWHXjzsrpYv55NGnALvKvpt9jo=",
    "TextBoxText":"見崎ちゃんかわいい",
    "CheckBoxBold":"on",
    "TextBoxBg":"#ffffff",
    "TextBoxColorA":"#7fbce8",
    "TextBoxColorB":"#4aa0e0",
    "DropDownListFont":"Tahoma",
    "DropDownListFontSize":"50",
    "DropDownListMirror":"0.9",
    "CheckBoxMirror":"on",
    "DropDownListSimbol":"none",
    "RadioButtonListPosition":"1",
    "DropDownListDPI":"300",
    "DropDownListType":"PNG",
    "ButtonCreate":"Create Logo",
}

class LogoCrawler(BaseCrawler):
    METHOD = "POST"

    def __init__(self, url, params=None):
        self.base_url = URL;
        self.params = PARAMS;

    def pre_crawling(self):
        print self.args
        self.params["TextBoxText"] = "%sちゃんかわいい" % self.args[1].encode("utf-8")

    def pre_scraping(self, html):
        pass

    def scraping(self, bs):
        image = bs.find(attrs={"id": "ImageLogo"})
        return image.attrs["src"];

    def save(self, result, db):
        id = self.args[0];
        html = urllib.urlopen("http://www.simwebsol.com/imagetool/" + result[2:]);
        f = open(IMAGE_BASE + str(id) + ".png", "w");
        f.write(html.read());

if __name__ == '__main__':
    LogoCrawler(URL, params=PARAMS).run(2, u"なでこ", method="POST")

