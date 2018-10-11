
try:
    nb = input("Rentrez le nombre\n")
    base_orig = int(input("Rentrez la base d'origine\n"))
    base_dest = int(input("Rentrez la base de destination\n"))

    assert 0 <= base_orig < 37 and 0 <= base_dest < 37

    for i, j in enumerate(nb):

        if ord('a') <= ord(j) <= ord('z'):

            tmpNb = list(nb)
            tmpNb[i] = (nb[i].upper())
            nb = ''.join(tmpNb)
                    
    listNb = list(str(nb))

    for i, j  in enumerate(listNb):
        if ord('A') <= ord(j) <= ord('Z'):
            listNb[i] = ord(j) - ord('A') + 10
        listNb[i] = int(listNb[i])

    for i in listNb:
        assert base_orig > int(i)

except ValueError as err:
    exit("Erreur de saisie")

except AssertionError:
    exit("Un des nombres est négatif ou n'est pas compatible avec sa base, ou une des bases est trop grande")


def conv(nb, base_orig, base_dest):

    """ Renvoie nb de la base base_orig dans la base base_dest """
    
    nb_10 = 0

    for i, valeur in enumerate(reversed(nb)):
        nb_10 += int(valeur) * (base_orig**i)

    nb_base_dest = []
    prem = False

    for i in range(37, -1, -1):
        for j in range(base_dest - 1, -1, -1):
            if nb_10 - (j * base_dest**i) >= 0 and (j!= 0 or prem == True):
                if j > 9:
                    j = chr(ord('A') + j - 10) 
                nb_base_dest.append(j)
                try:
                    nb_10 -= j * base_dest**i
                except TypeError:
                    nb_10 -= (ord(j) - ord('A') + 10) * base_dest**i
                prem = True
                break 

    nb_base_dest = [str(i) for i in nb_base_dest]
    nb_base_dest = ''.join(nb_base_dest)

    overflow = True

    for i in nb_base_dest:
        if str(i) != str(base_dest - 1) :
            overflow = False
            break

    if overflow:
        print("Attention : il est possible que le nombre soit trop grand pour être gérée dans cette base...")

    return nb_base_dest


print("{} (base {}) en base {} s'écrit : {}".format(nb, base_orig, base_dest, conv(listNb, base_orig, base_dest)))