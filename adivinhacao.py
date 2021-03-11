# Projeto jogo de adivinhação - Layout inicial do game
from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação", end="!\n")
print("*********************************")

tentativas_restantes = 5
numero_secreto = randint(0, 10)
chute_correto = False

while tentativas_restantes > 0 and chute_correto == False:

    chute = int(input("\nDigite o seu numero: "))
    print("Você digitou: {}".format(chute))

    acertou = (chute == numero_secreto)
    menor = (chute < numero_secreto)
    maior = (chute > numero_secreto)

    if acertou:
        chute_correto = True
        if chute_correto:
            print("Parabéns você acertou!")
            print("\nFim do Jogo")

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