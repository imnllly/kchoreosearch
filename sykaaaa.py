import requests
from bs4 import BeautifulSoup

URL = "https://www.youtube.com/watch?v=8j29aAbtYWo"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('span', attrs={'class': 'watch-title'})
print(title.text)

