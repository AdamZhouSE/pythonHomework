n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])
lists=[]
for i in range(pow(2,n)-1):
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
tree_layer=[]
for i in range(n):
    tree_layer.append(lists[pow(2,i)-1:pow(2,i+1)-1])
res_1=[]
for i in range(n):
    x=tree_layer[i].copy()
    res=0
    for a in range(len(x)):
        if(x[a]!="*"):
            res=a
            res_1.append(x[res])
            break
for i in range(n):
    x=tree_layer[i].copy()
    for a in range(len(x)):
        if(x[a]!="*"):
            if((tree_layer[i+1][2*a]=="*")&(tree_layer[i+1][2*a+1]=="*")):
                left=0
                right=0
                for y in range(len(x)):
                    if(x[y]!="*"):
                        left=y
                        break
                for y in range(len(x)-1,-1,-1):
                    if(x[y]!="*"):
                        right=y
                        break
                if((left!=a)&(right!=a)):
                    res_1.append(x[a])
for i in range(n-1,0,-1):
    x=tree_layer[i].copy()
    res=0
    for a in range(len(x)-1,-1,-1):
        if(x[a]!="*"):
            res=a
            res_1.append(x[res])
            break
print(*res_1)
print(*res_1,end="")

    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        