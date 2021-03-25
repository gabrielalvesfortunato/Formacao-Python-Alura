## MODULARIZANDO OS JOGOS ##
import adivinhacao
import forca

def choose_game():
    # Projeto de jogos - Layout inicial do game
    print("*********************************")
    print("*****Choose the game!*********", end="\n")
    print("*********************************")

    print("\n(1) Forca  (2) Adivinhação")

    game = int(input("\nWich game: "))

    if(game == 1):
        print("\nPLAYING HANGMAN...\n")
        forca.play()

    elif(game == 2):
        print("\nPLAYING GUESS GAME...\n")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    choose_game()