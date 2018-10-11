
inventaire = [
    ("pommmes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 76),
]

stock = []

for i in range(len(inventaire)):
    stock.append(inventaire[i][1])

stock.sort(reverse=True)
deja_fait = []

for i in range(len(inventaire)):
    for j in range(len(stock)):
        if stock[i] == inventaire[j][1] and j not in deja_fait:
            deja_fait.append(j)
            print(inventaire[j])


print([(fruit, qtt) for qtt, fruit in sorted([(qtt, fruit) for fruit, qtt in inventaire], reverse=True)])
#  C'est plus pratique avec les compréhensions de listes...
