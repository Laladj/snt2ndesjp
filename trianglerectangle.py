#on pourrait utiliser les tuples
from numpy import sqrt 
Xa = int(input("entrez votre valeur..."))
Ya = int(input("entrez votre valeur..."))
Xb = int(input("entrez votre valeur..."))
Yb = int(input("entrez votre valeur..."))
Xc = int(input("entrez votre valeur..."))
Yc = int(input("entrez votre valeur..."))

AB = sqrt((Xb-Xa)**2+(Ya-Yb)**2)
AC = sqrt((Xa-Xc)**2+(Ya-Yc)**2)
BC = sqrt((Xb-Xc)**2+(Yb-Yc)**2)

if BC**2 == AB**2+AC**2:
    print("le triangle est rectangle")
else: print("le triangle est quelconque")
