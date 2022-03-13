def palindrome(mot):
    mot = str(mot)  #pour ne pas avoir des soucis de guillemet
    mot = mot.lower()
    if mot == mot[::-1]: #regarder la documentation en cas de soucis https://docs.python.org/3/library/string.html
        return True

palindrome("kayak") 
