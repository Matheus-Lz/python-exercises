#Exercício 5 - Remover duplicatas, Escreva um programa que receba uma lista e retorne uma nova lista que contenha todos os elementos da primeira lista, menos as duplicadas.

def remove_duplicatas(lista):
    nova_lista = []
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista

lista_com_duplicatas = [1, 2, 3, 2, 4, 3, 5, 6, 5, 7, 8, 9, 8]
nova_lista = remove_duplicatas(lista_com_duplicatas)
print(nova_lista)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]