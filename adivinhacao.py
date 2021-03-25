# Importando o modulo que gera os numeros aleatoriamente
from random import randint

def play():
    # Projeto jogo de adivinhação - Layout inicial do game
    print("*********************************")
    print("  Welcome to the guessing game", end="!\n")
    print("*********************************")

    # Declarando as variaveis
    remaining_attempts = 0
    secret_number = randint(1, 50)
    correct_attempt = False
    points = 100

    print("\nWich difficulty level?")
    print("(1) Easy   (2) Normal   (3) Hard")

    level = int(input("\nChoose your difficulty: "))

    if level == 1:
        remaining_attempts = 10
    elif level == 2:
        remaining_attempts = 7
    elif level == 3:
        remaining_attempts = 5

    print("Number of attempts: {}".format(remaining_attempts))

    # Estrutura principal do programa
    for round in range(1, remaining_attempts + 1):
        attempt = int(input("\nEnter a number from 1 to 50: "))
        print("Your enter was: {}".format(attempt))

        # Definindo um intervalo valido de valores
        if(attempt < 1 or attempt > 50):
            print("You should enter a number from 1 to 50!")
            remaining_attempts = remaining_attempts - 1
            print("Remaining attempts: {}".format(remaining_attempts))
            continue

        # Definindo os criterios de validação
        rigth  = (attempt == secret_number)
        lesser = (attempt < secret_number)
        bigger = (attempt > secret_number)

        if rigth:
            print("\nCongratulations you win and make {} points!".format(points))
            print("\nGame Finished!")

        elif lesser:
            print("\nYour number is smaller than the right number, YOU WRONG!", end="\n")
            remaining_attempts = remaining_attempts - 1
            pontos_perdidos = abs(secret_number - attempt)
            points = points - pontos_perdidos
            print("Remaining attempts: {}".format(remaining_attempts))

        elif bigger:
            print("\nYour number is greater than the right number, YOU WRONG!", end="\n")
            remaining_attempts = remaining_attempts - 1
            pontos_perdidos = abs(secret_number - attempt)
            points = points - pontos_perdidos
            print("Remaining attempts: {}".format(remaining_attempts))

        if remaining_attempts == 0:
            print("\nYOU LOSE GAME OVER!")
            print("THE SECRECT NUMBER WAS: {}".format(secret_number))

if(__name__ == "__main__"):
    play()