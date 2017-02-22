def sum(a):
    b = 0
    for i in a:
        b= b+i
    return b

def mult (f):
    q=1
    for i in f:
        q=q*i
    return q

print (sum ([1,2,3,4]))
print (mult ([1,2,3,4]))