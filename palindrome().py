def palindrome(mot):
    mot = str(mot)  #pour ne pas avoir des soucis de guillemet
    mot = mot.lower()
    if mot == mot[::-1]: #regarder la documentation en cas de soucis https://docs.python.org/3/library/string.html
        return True

palindrome("kayak") 

def palindrome(mot):
    liste1, liste2 = [],[]
    for i in range(0,len(mot)):
        liste1.append(mot[i])
    for i in range(1, len(mot)+1):
        liste2.append(mot[-i])
    if liste1== liste2: 
        return True
    else:
        return False
palindrome(kayak)
