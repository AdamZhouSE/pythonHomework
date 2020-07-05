from itertools import combinations
n=int(input())
p=int(input())
jiandie=[]
starts=[]
for i in range(n):
    jiandie.append(0)
for i in range(p):
    x=input().split(" ")
    starts.append(int(x[0])-1)
    jiandie[int(x[0])-1]=int(x[1])
r=int(input())
sources=[]
for i in range(n):
    source=[]
    for j in range(n):
        source.append("0")
    sources.append(source)
for i in range(r):
    x=input().split(" ")
    sources[int(x[0])-1][int(x[1])-1]="1"
YES=[]
NO=[]
res=[]
for i in range(len(starts)):
    target=[]
    target.append(starts[i])
    ans=[]
    while(len(target)):
        x=target.copy()
        for a in target:
            x.pop(x.index(a))
            if not a in ans:
                ans.append(a)
                for j in range(len(sources[a])):
                    if sources[a][j]=="1":
                        if not j in ans and not j in x:
                            x.append(j)
        target=x
    res.append(ans)
targets=[]
targets.append(res[0])
res.pop(0)
for i in res:
    alls=[]
    for j in targets:
        if not j in alls:
            alls.append(j)
    for j in i:
        if not j in alls:
            targets.append(i)
            break
x=targets.copy()
for i in targets:
    delete=False
    for j in targets:
        if i!=j:
            is_in=True
            for k in i:
                if not k in j:
                    is_in=False
            if is_in:
                delete=True
    if delete:
        x.pop(x.index(i))
targets=x
alls=[]
for i in targets:
    for j in i:
        if not j in alls:
            alls.append(j)
if len(alls)<n:
    print("NO")
    for i in range(n):
        if not i in alls:
            print(i+1)
            break

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    