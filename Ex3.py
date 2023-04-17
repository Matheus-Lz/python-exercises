#Exercício 3 - Pedra, Papel, Tesoura , Faça um jogo de pedra, papel ou tesoura de dois jogadores. 
#(Dica: peça as jogadas ao usuário - usando input - compare-os, imprima uma mensagem parabenizando o vencedor e pergunte ao usuário se quer continuar jogando).

continuar_jogando = True

while continuar_jogando:
    # Pedir jogada do jogador 1
    jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
    while jogador1 not in ["pedra", "papel", "tesoura"]:
        jogador1 = input("Jogada inválida. Escolha pedra, papel ou tesoura: ").lower()

    # Pedir jogada do jogador 2
    jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()
    while jogador2 not in ["pedra", "papel", "tesoura"]:
        jogador2 = input("Jogada inválida. Escolha pedra, papel ou tesoura: ").lower()

    # Comparar jogadas e imprimir resultado
    if jogador1 == jogador2:
        print("Empate!")
    elif jogador1 == "pedra" and jogador2 == "tesoura" or jogador1 == "papel" and jogador2 == "pedra" or jogador1 == "tesoura" and jogador2 == "papel":
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

    # Perguntar se quer continuar jogando
    resposta = input("Quer continuar jogando? (sim/não)").lower()
    while resposta not in ["sim", "não"]:
        resposta = input("Resposta inválida. Quer continuar jogando? (sim/não)").lower()

    if resposta == "não":
        continuar_jogando = False

print("Obrigado por jogar!")