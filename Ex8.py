#Exercício 8, Use os pacotes BeautifulSoup e requests para imprimir uma lista de todos os títulos de artigos do New York Times.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

for headline in soup.find_all(class_='css-1qwxefa esl82me1'):
    print(headline.text.strip())