#on souhaite simuler mille fois au hasard une demande de pret 
import random as rd
def pret():
    oui = 0
    non = 0 
    for i in range(0,1000):
        if rd.randint(0,1) == 1:
            oui += 1
        else:
            non += 1
    return oui/10

def proportion(n):
    pourcentage = 0
    for i in range(1,n):
        x = pret()
        print(x)
        if x >= 60.0:
            pourcentage +=1 
    return pourcentage/10
proportion(10)
