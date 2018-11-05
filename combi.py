

def combi(s):
    if len(s) == 0:
        return [""]
    return append_bis(combi(s[1:len(s)]), s[0]) + combi(s[1:len(s)])



def append_bis(tab,a):
    if tab != None:       
        for i in range(len(tab)):
            tab[i] += a
    return tab
# s = "coucou"
# print(s[1:len(s)])

a = combi("abc")
print(a)