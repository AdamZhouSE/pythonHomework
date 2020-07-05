n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])
lists=[]
for i in range(pow(2,n)):
    lists.append("*")
sources=[]
try:
    while(True):
        x=input().split(" ")
        source=[]
        source.append(int(x[0]))
        source.append(int(x[1]))
        source.append(int(x[2]))
        sources.append(source)
except(EOFError):
    pass
print(sources)
lists[0]=sources[0][0]
for i in sources:
    for a in range(len(lists)):
        if(lists[a]==i[0]):
            if(i[1]!=0):
                lists[2*a+1]=i[1]
            if(i[2]!=0):
                lists[2*a+2]=i[2]
        break
print(lists)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        