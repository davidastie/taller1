def inv(c):
    d = ""
    x = len(c)
    s = -1
    while x >= 1:
        d=d+c[s]
        s= s-1
        x= x-1
    return d

a = raw_input(" Ingrese una palabra ")
print inv(a)