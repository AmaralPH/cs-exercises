import requests


URL = " https://api.github.com/users"


response = requests.get(URL)


for item in response.json():
    print(f"{item['login']} {item['url']}")
