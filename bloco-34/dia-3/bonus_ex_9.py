import requests


URL = "http://quotes.toscrape.com/api/quotes?page="
page = 1
has_next = True
quotes_list = []

while has_next:
  response = requests.get(URL + f"{page}").json()
  for quote in response["quotes"]:
      quotes_list.append(quote["text"])
  has_next = response["has_next"]
  page += 1


print(len(quotes_list))


with open("quotes.txt", "w") as file:
    for quote in quotes_list:
        file.write(f"{quote}\n")


# print(quotes_list)