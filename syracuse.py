def syracuse(n):
    i=0
    while n!=1:
        print(n) 
        if n%2==0: 
            n = n//2 
        else:
            n = 3*n+1
        
        i+=1
    print("Le 1 a été trouvé apres", i,"iterations!")
   

syracuse(15)