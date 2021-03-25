import random

# Inicializa o jogo
def play():

    starter_layout()
    correct_word = secret_word_initialization()
    correct_letters = correct_letters_initialize(correct_word)

    hanged = False
    complete = False
    erros = 0

    print(correct_word)

    # Enquanto(True)
    while not hanged and not complete:

        letters_remaining = correct_letters.count("_")

        print("\n\n{}  Letters ramaining: {}".format(correct_letters, letters_remaining))
        attempt = make_attempt()

        # Se a tentativa estiver dentre as letras da palavra correta
        if attempt in correct_word:
            draw_gallows(erros)
            correct_attmept(attempt, correct_word, correct_letters, letters_remaining)

        # Se a tentativa nao estiver dentre as letras da palavra correta
        else:
            erros += 1
            draw_gallows(erros)

        acertou = "_" not in correct_letters

        # Se as letras restantes chegarem a 0 ou seja a palavra foi completa
        if acertou:
            winner_message(correct_letters, letters_remaining - 1)
            complete = True

        if erros == 7:
            loser_message(correct_word)
            hanged = True


#Projeto jogo da Forca - Layout inicial do game
def starter_layout():
    print("***************************")
    print("Welcome to the Hangman game!", end="!\n")
    print("***************************")


# Inicializa a palavra da Forca
def secret_word_initialization():
    words = []

    with open("palavras.txt", "r") as file:
        for word in file:
            word = word.strip()
            words.append(word)

    correct_word = random.choice(words).upper()
    return correct_word


# Inicializa o campo das letras
def correct_letters_initialize(correct_word):
    return ["_" for letters in correct_word]


def make_attempt():
    attempt = input("\nType a letter: ")
    return attempt.strip().upper()


def correct_attmept(attempt, correct_word, correct_letters, letters_remaining):
    index = 0
    for letter in correct_word:
        if attempt.upper() == letter.upper():
            correct_letters[index] = letter
        index = index + 1


def loser_message(correct_word):
    print("\nYOU ARE HANGED :( \nYOU LOSE!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("\n\nTHE CORRECT WORD WAS: {}".format(correct_word))


def winner_message(correct_letters, letters_remaining):
    print("\n\n{}  Letters ramaining: {}".format(correct_letters, letters_remaining))
    print("\nCONGRATULATIONS YOU WIN!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def draw_gallows(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == '__main__':
    play()