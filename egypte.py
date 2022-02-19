def egypte(a,b):
    c = 0
    if(a>=b):
        while a != 0:
            if a % 2 == 1:
                c = c+b
            a = a//2
            b += b
    else:
        print("a doit etre plus grand que b")
    return c


res=egypte(234,37)
print("La muliplication egyptienne de 234 et 37 est",res)