
import random
NBNOEUDS = 25 

class Noeud:

    def __init__(self, val):
        self.val = val 
        self.fg = None
        self.fd = None


def placerValABR(noeud, val):
    if val <= noeud.val:
        if noeud.fg == None:
            noeud.fg = Noeud(val)
        else :
            placerValABR(noeud.fg, val)
    else:
        if noeud.fd == None:
            noeud.fd == Noeud(val)
        else:
            placerValABR(noeud.fd, val)


def creerABR():
        listeNoeuds = []
        for i in range(25):
            listeNoeuds.append(random.randint(0, 150))
        racine = Noeud(listeNoeuds[0])
        print("Il y a", len(listeNoeuds, " valeurs")
        for i in range(1, len(listeNoeuds)):
            print("traitement de la val", i)
            placerValABR(racine, listeNoeuds[i])
        return racine

def parcoursInfixe(racine):
    if racine!= None:
        parcoursInfixe(racine.fg)
        print(racine.val)
        parcoursInfixe(racine.fd)



def supprimer(ABR, val):
    feuilleASupp = ABR 
    while feuilleASupp.val != val:
        feuilleASupp = feuilleASupp.fd if (feuilleASupp > val) else feuilleASupp.fg
    fMin = feuilleASupp.fd
    pereMin = feuilleASupp
    if fMin != None:
        while pereMin.fg.fg != None:
            pereMin = pereMin.fg
            fMin = pereMin.fg
        pereMin.fg = fMin.fd
    feuilleASupp.val = fMin.val


def moha():
    # function

if __name__ == '__main__':
    arbre = creerABR()
    parcoursInfixe(arbre)
    supprimer(arbre, arbre.val)
    print("\n\n")
    parcoursInfixe(arbre)
    moah()




    