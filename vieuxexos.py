    a = float(input("entrez le nombre a: "))
    b = float(input("entrez le nombre b: "))
    c = float(input("entrez le nombre c: "))

    if a != 0:
        x = (c-b)/a
    else: x = b
    print(x)



    #exo 2
    n = int(input("entrez le nombre n: "))
    for i in range(1,n):
        n = n+i
        print(n)
    print(n)
    #########################################
    def sommeDesFractions(n):
        i = 1
        s = 0.0
        for i in range(1, n+1):
            s = s + 1/i;
        return s;
    

    n= int(input("entre ta valeur "))
    print("sommeDesFractions est", round(sommeDesFractions(n), 6))
