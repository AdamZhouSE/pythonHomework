class Structure:
    def __init__(self):
        self.data=[]
    def add(self,a):
        self.data.append(a)
        
    def remove(self,a):
        loc=self.data.index(a)
        self.data.pop(loc)
    def query_rank(self,x):
        self.data.sort()
        return self.data.index(x)+1
    def query_number(self,rank):
        self.data.sort()
        return self.data[rank-1]
    def query_bef(self,x):
        self.data.sort(reverse=True)
        for k in self.data:
            if k<x:
                return k
    
        
    def query_suc(self,x):
        self.data.sort()
        for k in self.data:
            if k>x:
                return k
    
    
a=int(input().strip())
structure=Structure()
for i in range(a):
    line=input().strip()
    option=int(line.split()[0])
    num=int(line.split()[1])
    if option==1:
        structure.add(num)
    elif option==2:
        structure.remove(num)
    elif option==3:
        print(structure.query_rank(num))
    elif option==4:
        print(structure.query_number(num))
    elif option==5:
        print(structure.query_bef(num))
    else:
        print(structure.query_suc(num))
        
        
        
        
        
        
        