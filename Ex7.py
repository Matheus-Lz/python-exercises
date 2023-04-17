#Exercício 7 - Leitura de arquivos, Dado um arquivo .txt que contem uma lista de nomes, conte quantas vezes cada nome aparece no arquivo e imprima os resultados na tela. 
#Um arquivo nomes.txt é fornecido junto a esse repositório.

with open('names.txt', 'r') as arquivo:
    nomes = arquivo.read().splitlines()

contador = {}

for nome in nomes:
    if nome in contador:
        contador[nome] += 1
    else:
        contador[nome] = 1

for nome, quantidade in contador.items():
    print(f"{nome}: {quantidade}")