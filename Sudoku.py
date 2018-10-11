
tab = [[0]*9 for i in range(9)]


for i in range(len(tab)):
    for j in range(len(tab[0])):

        valide = True
        while valide:
            saisie = input("Rentrez la case ligne {}, colonne {} (0 si vide)\n".format(i + 1, j + 1))
            try:
                nb = int(saisie)
                assert(0 <= nb < 10)
                tab[i][j] = str(nb)
                valide = False
            except ValueError as err:
                print("dsl ce n'est pas un nombre valable : ", err)
            except AssertionError:
                print("Ce n'est pas un chiffre entre 0 et 10 (exclus)")


for i in tab:
    print(" | ".join(str(i)))
