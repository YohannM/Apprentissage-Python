
def afficher_flottant(nombre):
    if type(nombre) is not float:
        raise TypeError("On veut un flottant")
    tmp = str(nombre).split(".")
    tmp[1] = tmp[1][:3]
    print(",".join(tmp))


afficher_flottant(3.8959898)
afficher_flottant(458.9898)
afficher_flottant(0.56)

