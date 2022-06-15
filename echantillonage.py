#on souhaite faire n fois 100 tirages d'une piece, pour etudier combien d'echantillons
import random
import math
def echan(n: int):
    N_en_dessous_de_95, N_au_dessus_de_95, somme, pourcentage_en_dehors = 0,0,0,0
    liste_des_frequences =  []
    for _ in range(0,n):
        somme = 0
        for x in range(0,100): #on va etudier le nombre de fois que pile cad 1 tombe
            somme += random.randint(0,1)
        liste_des_frequences.append(somme /100)
    print(liste_des_frequences)
    for frequence in liste_des_frequences:
        if frequence < 0.5 - 1/math.sqrt(n):
            N_en_dessous_de_95 += 1
        elif frequence > 0.5 + 1/math.sqrt(n):
            N_au_dessus_de_95 += 1
        else : pass
    #print(f"pourcentage de valeurs en dessous de l'intervalle: ",(N_en_dessous_de_95/n)*100,"pourcentage de valeurs au dessus: ",(N_au_dessus_de_95/n)*100)
    pourcentage_en_dehors = (N_en_dessous_de_95/n)*100 + (N_au_dessus_de_95/n)*100
    print(0.5 - 1/math.sqrt(n))
    print(0.5 + 1/math.sqrt(n))
    return pourcentage_en_dehors
echan(500)
