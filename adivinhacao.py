# Importando o modulo que gera os numeros aleatoriamente
from random import randint

# Projeto jogo de adivinhação - Layout inicial do game
print("*********************************")
print("Bem vindo ao jogo de Adivinhação", end="!\n")
print("*********************************")

# Declarando as variaveis
tentativas_restantes = 5
numero_secreto = randint(0, 20)
chute_correto = False

# Estrutura principal do programa
for rodada in range(1, tentativas_restantes + 1):
    chute = int(input("\nDigite um número entre 1 e 20: "))
    print("Você digitou: {}".format(chute))

    if(chute < 1 or chute > 20):
        print("Você deve digitar um numero entre 1 e 20!")
        continue

    # Definindo os criterios de validação
    acertou = (chute == numero_secreto)
    menor = (chute < numero_secreto)
    maior = (chute > numero_secreto)

    if acertou:
        print("Parabéns você acertou!")
        print("\nFim do Jogo")
        break

    elif menor:
        print("\nO seu valor foi menor que o numero correto, VOCE ERROU!", end="\n")
        tentativas_restantes = tentativas_restantes - 1
        print("Tentativas Restantes: {}".format(tentativas_restantes))

    elif maior:
        print("\nO seu valor foi maior que o numero correto, VOCE ERROU!", end="\n")
        tentativas_restantes = tentativas_restantes - 1
        print("Tentativas Restantes: {}".format(tentativas_restantes))

    if tentativas_restantes == 0:
        print("\nVOCÊ PERDEU FIM DE JOGO!")
        print("O NÚMERO SECRETO ERA: {}".format(numero_secreto))