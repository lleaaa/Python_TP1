def syracuse(N,n):
    u = N
    
    for i in range(1, n+1): 
        if u%2==0: 
            u = u//2 
        else:
            u = 3*u+1
        print(u)
   

syracuse(15,5)