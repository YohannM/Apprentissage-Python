def affiche(*param, sep=' ', fin='\n'):

    param = list(param)

    for i, p in enumerate(param):
        param[i] = str(p)

    stri = sep.join(param)
    stri += fin
    print(stri)

affiche("coucou moi c'est yoh j'ai", 17, "ans")