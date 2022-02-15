import requests
from parsel import Selector


URL = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"


response = requests.get(URL)
selector = Selector(text=response.text)


title = selector.css("h1::text").get()
price = selector.css(".price_color").re_first(r"\d+\.\d{2}")
description = selector.css("#product_description ~ p::text").get()
suffix = "...more"
if description.endswith(suffix):
    description = description[:-len(suffix)]
cover = selector.css("img::attr(src)").get()
cover_url = "http://books.toscrape.com/catalogue/" + cover
stock = selector.css(".instock").re(r"\d+")[0]

print(f"{title},{price},{description},{cover_url},{stock}")