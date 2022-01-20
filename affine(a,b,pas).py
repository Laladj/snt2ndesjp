def affine(a,b,entree,sortie,pas):
    for x in range(entree,sortie+1, pas):
        print(x , " : ", a*x+b)
affine(2,3,1,10,2)
