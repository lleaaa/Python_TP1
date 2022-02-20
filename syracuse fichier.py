class Syr:
    def __init__(self,n):
        self.n=n
    def get(self):
        return self.n
    def estpair(self):
        return self.n%2==0
    def pair(self):
        self.n=self.n//2
        return self.n
    def impair(self):
        self.n=3*self.n+1
        return self.n
    def iteration(self):
        return self.n!=1
def syracuse(namefile):
    with open(namefile, 'r') as f:
        n=list(map(int,f.readlines()))
        x = Syr(n[0])
        i=0
        while x.iteration():
             
            if x.estpair(): 
                x.pair() 
            else:
                x.impair()
            
            i+=1
            with open(namefile, 'a') as f:
                f.write("\n"+str(x.get()))
            
        print("Le 1 a été trouvé apres", i,"iterations!")
        f.close()   
   
syracuse("test.txt")