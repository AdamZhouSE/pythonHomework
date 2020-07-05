class Structure:
    def __init__(self,data):
        self.data=data
    def query_rank(self,l,r,x):
        t=self.data[l-1:r]
        t.sort()
        return t.index(x)+1
    def query_number(self,l,r,k):
        t=self.data[l-1:r]
        t.sort()
        return t[k-1]
    def update(self,pos,x):
        self.data[pos-1]=x
    def query_bef(self,l,r,x):
        t=self.data[l-1:r]
        t.sort(reverse=True)
        for i in t:
            if i<x:
                return i
        return 0
    def query_suc(self,l,r,x):
        t=self.data[l-1:r]
        t.sort()
        for i in t:
            if i>x:
                return i
        return 0
    
    
line1=input().strip()
length=int(line1.split()[0])
times=int(line1.split()[1])
s=[int(x) for x in input().strip().split()]
structure=Structure(s)
for i in range(times):
    line=input().strip()
    if int(line.split()[0])==1:
        print(structure.query_rank(int(line.split()[1]),int(line.split()[2]),int(line.split()[3])))
    elif int(line.split()[0])==2:
        print(structure.query_number(int(line.split()[1]),int(line.split()[2]),int(line.split()[3])))
    elif int(line.split()[0])==3:
        structure.update(int(line.split()[1]),int(line.split()[2]))
    elif int(line.split()[0])==4:
        print(structure.query_bef(int(line.split()[1]),int(line.split()[2]),int(line.split()[3])))
    else:
        print(structure.query_suc(int(line.split()[1]),int(line.split()[2]),int(line.split()[3])))
    
    
    
    