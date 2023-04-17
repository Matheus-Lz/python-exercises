#Exercício 9 - Gravar um arquivo, Pegue o código do exercício anterior e ao invés de imprimir os resultados na tela, escreva-os em um arquivo txt.
#No seu código você pode deixar o nome do arquivo hard-coded.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

with open('nyt_titles.txt', 'w') as file:
    for headline in soup.find_all(class_='css-1qwxefa esl82me1'):
        file.write(headline.text.strip() + '\n')