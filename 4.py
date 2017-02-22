def caracter(z):
    if z== "a" or z== "e" or z== "i" or z== "o" or z== "u":
         return True
    elif z== "A" or z== "E" or z== "I" or z== "O" or z== "U":
         return True
    else :
        return False

a:raw_input(" Ingrese una letra ")
print caracter ("E")
