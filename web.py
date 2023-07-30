import requests
from bs4 import BeautifulSoup
class PriceTracer:
    def __init__(self, url):
        self.url=url
        self.useragent={"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"}
        self.response=requests.get(url=self.url, headers=self.useragent).text
        self.soup=BeautifulSoup(self.response,"lxml")
    def product_title(self):
        title=self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"
    def product_price(self):
        price=self.soup.find("span",{"id":"priceblock.ourprice"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag Not Found"

device=PriceTracer(url="https://www.amazon.in/dp/B0BZYTVPR2/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=4f2653811f2f13865258bc529563bd91&content-id=amzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d%3Aamzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d&hsa_cr_id=0&pd_rd_plhdr=t&pd_rd_r=28ed7080-09ef-430e-b74c-1970c622ae23&pd_rd_w=4Q8Kr&pd_rd_wg=o6QTZ&qid=1690561084&ref_=sbx_be_s_sparkle_lsi4d_asin_0_img&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987")
print(device.product_title())
print(device.product_price())
