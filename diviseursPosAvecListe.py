def diviseurs(a):
    liste = []
    for i in range(1,a+1):
        if a%i == 0:
            liste.append(i) #on ajoute i a la liste
        else: pass
    return liste          
