def inv(c):
    d = ""
    x = len(c)
    s = -1
    while x >= 1:
        d=d+c[s]
        s= s-1
        x= x-1
    return d

def palindromo (c):
    pol =inv(c)
    s = 0
    p = 0
    for i in range(len(c)):
        if pol[s]==c[s]:
            s = s+1
            p = p+1

    if p==len(c):
        print (" Es palindrome ")
    else :
        print (" No es palindrome ")


a = raw_input(" Ingrese una palabra ")
palindromo(a)