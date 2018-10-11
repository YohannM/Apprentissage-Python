import os

annee = input("Rentrez une année\n")

try:
    annee = int(annee)
    assert annee >= 0
    if annee == 0:
        raise ValueError("L'année est égale à 0")
except AssertionError:
    print("Erreur : annee < 0")
except ValueError as err2:
    print("Erreur : ", err2)
else:
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année ", annee, " est bissextile.")
    else:
        print("L'année ", annee, " n'est pas bissextile.")

    os.system("pause")
