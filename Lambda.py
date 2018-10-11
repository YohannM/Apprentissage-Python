
carre = lambda a: a*a

print(carre(8))


def divise (x=2, y=10):
    """ Cette fonction prend en paramètre deux entiers
        et détermine si le premier divise le deuxième.
        La valeur par défaut du premier entier est 2 :
        passer y déterminera donc sa parité
    """
    if y % x == 0:
        print(x, " divise ",y)
    else:
        print(x, " ne divise pas ",y)


divise(4,8)

divise(y=8,x=4)

divise(2)

divise(y=5)

help(divise)