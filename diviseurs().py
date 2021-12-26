def diviseurs(x):
    x = int(x)
    
    print("les diviseurs de",x,"sont ")
    if x > 0: #SI x est positif
        for i in range(1,x+1):
            if x % i == 0: 
                print(i)
            
    
    elif x < 0: #si X est negatif
        for i in range(x,0):
            if x % i == 0: 
                print(i)
        
