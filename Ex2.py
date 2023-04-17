#Exercício 2 - Palíndromos, peça uma string qualquer ao usuário e informe a ele se a string é um palíndromo ou não. 

string = input("Digite uma palavra: ")

if string == string[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")