import requests


URL_BASE = "https://scrapethissite.com/pages/advanced/?gotcha=headers"


headers = {
    'authority': 'www.scrapethissite.com',
    'method': 'GET',
    'path': '/pages/advanced/?gotcha=headers',
    'scheme': 'https',
    'accept': "text/html",
    'accept-encoding': "gzip, deflate, br",
}


response = requests.get(URL_BASE, headers=headers)
print(response)
assert "bot detected" not in response.text