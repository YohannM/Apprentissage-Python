from random import randrange
from math import ceil

jouer = True
cagnote = 50

print("Votre cagnote est de ", cagnote)

while cagnote > 0 and jouer:

    mise = numero = input("Rentrez une mise de 1 à votre cagnote\n")

    try:
        mise = int(mise)
        if mise <= 0 or mise > cagnote:
            raise ValueError("Mise trop grande ou trop petite")
    except ValueError as err:
        print ("Erreur :", err)
        continue

    numero = input("Rentrez votre numéro de 0 à 49\n")

    try:
        if numero == "20":
                raise ValueError("j'aime pas le numéro 20")
        numero = int(numero)
        assert numero > -1 and numero < 50
    except AssertionError:
        print("Non compris dans la borne")
        continue
    except ValueError as err:
        print("Erreur : ", err)
        continue
    else:
        print("Numero correct")

    num_tire = randrange(50)
    print("Numéro tiré : ", num_tire)

    if numero % 2 == num_tire % 2:
        if numero == num_tire:
            print("Victoire")
            mise *= 3
        else:
            print("Meme couleur")
            mise = ceil(mise * 0.5)
    else:
        print("Dommage")
        mise *= -1

    cagnote += mise

    print("Votre cagnote est de ", cagnote)

    if cagnote <= 0:
        print("Vous êtes ruiné")
        jouer = False
    else:
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? \n")

        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            jouer = False

print("Fin de la partie !")
