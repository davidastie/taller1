def lista (a,b):
    for i in a:
        for q in b:
            if i == q:
                return True
    return False

w = raw_input(" Ingresar palabra 1 ")
r = raw_input(" Ingrese palabra 2 ")
print lista(w,r)
