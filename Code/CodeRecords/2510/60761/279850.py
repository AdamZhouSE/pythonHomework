def adddig(x,z,levels,n):
    add=[0 for i in range(n)]
    for i in range(len(levels)):
        if(levels[i][0]==x):
            for j in levels[i][1]:
                add[j-1]+=z
                temp=adddig(j,z,levels,n)
                for i in range(n):
                    add[i]+=temp[i]
            break
    return add
def addsum(x,levels,digits):
    add=0
    for i in range(len(levels)):
        if(levels[i][0]==x):
            for j in levels[i][1]:
                add+=digits[j-1]+addsum(j,levels,digits)
            break
    return add
n,m,r,p=map(int,input().split(" "))
digits=list(map(int,input().strip().split(" ")))
edges=[]
for i in range(n-1):
    x,y=map(int,input().split(" "))
    edges.append([x,y])
levels=[]
levels.append([r])
while(len(edges)>0):
    j=len(levels)-1
    k=0
    i=0
    while(i<len(edges)):
        if(edges[i][0]==levels[j][0]):
            if(len(levels[j])==1):
                levels[j].append([edges[i][1]])
            else:
                levels[j][1].append(edges[i][1])
            edges.pop(i)
            k=1
            break
        elif(edges[i][1]==levels[j][0]):
            if(len(levels[j])==1):
                levels[j].append([edges[i][0]])
            else:
                levels[j][1].append(edges[i][0])
            edges.pop(i)
            k=1
            break
        else:
            i+=1
    if(k==0):
        if(len(levels[j])>1):
            for s in levels[j][1]:
                levels.append([s])
for i in range(m):
    string=input()
    if(string.startswith('1')):
        x,y,z=map(int,string[2:].split(" "))
        while(y!=x):
            k=0
            for j in range(len(levels)):
                if(y in levels[j][1]):
                    digits[levels[j][0]-1]+=z
                    y=levels[j][0]
                    k=1
                    break
            if(k==0):
                x=x+y
                y=x-y
                x=x-y
        digits[x-1]+=z        
    elif(string.startswith('2')):
        x,y=map(int,string[2:].split(" "))
        add=[0 for k in range(len(digits))]
        add[y-1]=digits[y-1]
        while(y!=x):
            for j in range(len(levels)):
                if(y in levels[j][1]):
                    add[levels[j][0]-1]=digits[levels[j][0]-1]
                    y=levels[j][0]
                    break
        print(sum(add)%p)
        
    elif(string.startswith('3')):
        x,z=map(int,string[2:].split(" "))
        digits[x-1]+=z
        add=adddig(x,z,levels[:],n)
        for k in range(n):
            digits[k]+=add[k]
    else:
        x=int(string[2:])
        add=addsum(x,levels[:],digits)
        add+=digits[x-1]
        print(add%p)
    
    
    
    
    
    
    
    
    
    
    
    