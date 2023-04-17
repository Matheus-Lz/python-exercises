#Exercício 6 - Gerador de Senhas,Escreva um gerador de senhas em python. Seja criativo com a forma de gerar senhas,
#Senhas fortes possuem uma mistura de letras minúsculas, maiúsculas, números e símbolos.
#As senhas devem ser aleatórioas, gerando uma nova senha a cada vez que o usuário executar o programa.

import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

nova_senha = gerar_senha()
print(nova_senha)