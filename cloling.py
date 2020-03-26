import requests
from bs4 import BeautifulSoup



for i in range(1,20):
    site = "https://finance.naver.com/sise/entryJongmok.nhn?&page=" + str(i)

    response = requests.get(site)

    html = response.text

    soup = BeautifulSoup(html,'html.parser')

    for tag in soup.select('td[class]'):
        print(tag.text)

