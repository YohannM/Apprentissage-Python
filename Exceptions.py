
denominateur = 0

try:
    a = 1 / denominateur
except NameError as err:
    print("Erreur : ", err)
except ZeroDivisionError as err2:
    print("Erreur : ", err2)
    exit()
except TypeError:
    pass
else:
    print(a)
finally:
    print("Fin")
