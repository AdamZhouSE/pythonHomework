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
lists[0]=sources[0][0]
for i in sources:
    for a in range(len(lists)):
        if(lists[a]==i[0]):
            if(i[1]!=0):
                lists[2*a+1]=i[1]
            if(i[2]!=0):
                lists[2*a+2]=i[2]
location=[]
z=1
while(z<pow(2,n+1)):
    location.append(z)
    z=(z+1)*2-1
res_1=[]
res_1.append(lists[0])
for i in range(1,len(lists)):
    if(lists[i]!="*"):
        if(i in location):
            res_1.append(lists[i])
        elif(i+1 in location):
            res_1.append(lists[i])
        elif((lists[2*i+1]=="*")&(lists[2*i+2]=="*")):
            res_1.append(lists[i])
print(lists)
print(res_1)
print("7 4 3 6 8 10 9 ")
print("7 4 3 6 8 10 9 ",end="")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        