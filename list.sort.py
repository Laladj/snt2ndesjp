import random 
liste = []
for element in range(10): 
    liste.append(random.randint(0,10))
for _ in range(0,10):
    for i in range(0,9):
        if liste[i] > liste[i+1]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
    print(liste)
print(liste)
