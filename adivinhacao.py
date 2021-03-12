# Importando o modulo que gera os numeros aleatoriamente
from random import randint

# Projeto jogo de adivinhação - Layout inicial do game
print("*********************************")
print("Bem vindo ao jogo de Adivinhação", end="!\n")
print("*********************************")

# Declarando as variaveis
tentativas_restantes = 0
numero_secreto = randint(1, 50)
chute_correto = False
pontos = 100

print("\nQual o nivel de dificuldade?")
print("(1) Facil   (2) Medio   (3) Difícil")

nivel = int(input("\nDefina o nível: "))

if nivel == 1:
    tentativas_restantes = 10
elif nivel == 2:
    tentativas_restantes = 7
elif nivel == 3:
    tentativas_restantes = 5

print("Número de Tentativas: {}".format(tentativas_restantes))

# Estrutura principal do programa
for rodada in range(1, tentativas_restantes + 1):
    chute = int(input("\nDigite um número entre 1 e 50: "))
    print("Você digitou: {}".format(chute))

    # Definindo um intervalo valido de valores
    if(chute < 1 or chute > 50):
        print("Você deve digitar um numero entre 1 e 50!")
        tentativas_restantes = tentativas_restantes - 1
        print("Tentativas Restantes: {}".format(tentativas_restantes))
        continue

    # Definindo os criterios de validação
    acertou = (chute == numero_secreto)
    menor = (chute < numero_secreto)
    maior = (chute > numero_secreto)

    if acertou:
        print("\nParabéns você acertou e fez um total de {} pontos!".format(pontos))
        print("\nFim do Jogo")
        break

    elif menor:
        print("\nO seu valor foi menor que o numero correto, VOCE ERROU!", end="\n")
        tentativas_restantes = tentativas_restantes - 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        print("Tentativas Restantes: {}".format(tentativas_restantes))


    elif maior:
        print("\nO seu valor foi maior que o numero correto, VOCE ERROU!", end="\n")
        tentativas_restantes = tentativas_restantes - 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        print("Tentativas Restantes: {}".format(tentativas_restantes))

    if tentativas_restantes == 0:
        print("\nVOCÊ PERDEU FIM DE JOGO!")
        print("O NÚMERO SECRETO ERA: {}".format(numero_secreto))