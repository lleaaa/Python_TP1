def egypte(a,b):
    A = a
    B = b
    c = 0
    if(A>=B):
        while A != 0:
            if A % 2 == 1:
                c = c+B
            A = A//2
            B = B*2
    else:
        print("a doit etre plus grand que b")
    return c


res=egypte(234,37)
print("La muliplication egyptienne de 234 et 37 est",res)