## MODULARIZANDO OS JOGOS ##
import adivinhacao
import forca

def escolhe_jogo():
    # Projeto de jogos - Layout inicial do game
    print("*********************************")
    print("*****Escolha o seu jogo!*********", end="\n")
    print("*********************************")

    print("\n(1) Forca  (2) Adivinhação")

    jogo = int(input("\nQual Jogo: "))

    if(jogo == 1):
        print("\nJOGANDO FORCA...\n")
        forca.jogar()

    elif(jogo == 2):
        print("\nJOGANDO ADIVINHAÇÃO...\n")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()