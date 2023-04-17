#Exercício 4 - Jogo da adivinhação, Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). Peça ao usuário para adivinhar o número, e então diga se a tentativa foi menor, maior ou correta. 
# (Dica: lembre-se de usar o input dos exercícios anteriores). Mantenha o jogo executando até que o usuário digite "sair".
import random

while True:
    # Gerar número aleatório
    numero_aleatorio = random.randint(1, 9)

    # Pedir ao usuário para adivinhar o número
    resposta = input("Adivinhe o número entre 1 e 9 (ou digite 'sair' para encerrar o jogo): ")

    # Verificar se o usuário quer sair
    if resposta.lower() == "sair":
        print("Obrigado por jogar!")
        break

    # Converter a resposta do usuário em um número inteiro
    try:
        tentativa = int(resposta)
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue

    # Verificar se a tentativa é menor, maior ou igual ao número aleatório
    if tentativa < numero_aleatorio:
        print("Tente novamente. O número é maior.")
    elif tentativa > numero_aleatorio:
        print("Tente novamente. O número é menor.")
    else:
        print("Parabéns! Você adivinhou o número!")