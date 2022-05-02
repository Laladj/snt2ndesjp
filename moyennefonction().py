#notre objectif est de trouver la valeur moyenne d'une fonction avec un intervalle defini et une precision definie

def moyennefonction(fonction,a,b,precision):
    """
    fonction: fonction a evaluer : mettre lambda x: + la fonction a evaluer.
    a: borne inferieure de l'intervalle
    b: borne superieure de l'intervalle
    precision: precision desiree
    """
    n = 0
    somme = 0
    while (b-a)>precision:
        n += 1
        somme += fonction(a+((b-a)/n))
        a += (b-a)/n
    return somme/n
moyennefonction(lambda x:x**2,0,3,0.00001) 
#1/3 integral_0^3 x^2 dx = 3 , ainsi, la moyenne de la fonction est 3. le programme est verifie
