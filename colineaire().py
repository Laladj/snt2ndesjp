#demontrer que trois points sont alignés xx' = yy'
#on commence par etablir les variables des vecteurs
Xa = int(input("entrez le point "))
Ya = int(input("entrez le point "))
Xb = int(input("entrez le point "))
Yb = int(input("entrez le point "))
Xc = int(input("entrez le point "))
Yc = int(input("entrez le point "))

#coord du vecteur ab xb-xa yb- ya
Xab= Xb - Xa
Yab= Yb - Ya
Xbc = Xc-Xb
Ybc = Yc - Yb

if Xab*Xbc == Yab*Ybc:
    aligné= True
else: aligné= False
print(aligné)
################################################################################################
#maniere plus elegante
def collineaire(x1, y1, x2, y2, x3, y3):
     
    
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
 
    if (a == 0):
        print "Yes"
    else:
        print "No"
 
