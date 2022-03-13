portee = int(input("veuillez entrer la portee "))
liste = []
for i in range(0,portee+1):
    liste.append(i)
print(liste)
resultat = [(val, pow(val, 2)) for val in liste] 
print(resultat)
