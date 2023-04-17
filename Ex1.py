#Exercício 1 - Par ou Ímpar, peça ao usuário um número. Retorne a ele se o número é par ou impar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")