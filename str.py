prenom = ["Yohann", "Sarah", "Mathilde", "René"]
nom = ["marmonier", "Sarazzin", "chenet", "franceau"]
age = [17, 15, 19, 22]

presentation = "Je m'appelle {} {} et j'ai {} ans"

a = list(zip(prenom, nom, age))
print(a, "\n")

for i, j, k in zip(prenom, nom, age):  # 3-uplets
    print(presentation.format(i, j.capitalize(), k))
    print("Enregistré : {p} {n} {a}\n".format(p=i, n=j.capitalize(), a=k))