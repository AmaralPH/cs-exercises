import requests
from parsel import Selector


URL = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"
URL_BASE = "https://en.wikipedia.org"

response = requests.get(URL)
selector = Selector(text=response.text)


flags_url = selector.css(".gallery .image img::attr(src)").getall()
for flag_url in flags_url:
    filename = flag_url.split("/")[-1]
    image_content = requests.get("https:" + flag_url).content
    with open(f"./flags/{filename}", "wb") as file:
        file.write(image_content)