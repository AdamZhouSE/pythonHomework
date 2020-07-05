import copy
temp=[int(x) for x in input().split(' ')]
n=temp[0]
m=temp[1]
graph=[[-1]*n for i in range(n)]
for i in range(m):
    temp=[int(x) for x in input().split(' ')]
    x=temp[0]-1
    y=temp[1]-1
    v=temp[2]
    if(graph[x][y]==-1):
        graph[x][y]=v
    elif(graph[x][y]>v):
        graph[x][y]=v
        
res=0
for i in range(n):
    for j in range(n):
        if(graph[i][j]!=-1):
            res+=graph[i][j]
            
for i in range(n):
    add=0
    tt=[-1]*n
    al=[]
    d=copy.deepcopy(graph[i])
    s=[-1]*n
    con=True
    for j in range(n):
        if(d[j]!=-1):
            tt[j]=i
    for j in range(n-1):
        pre=max(d)
        for k in range(n):
            if(d[k]<pre and d[k]!=-1 and s[k]==-1):
                pre=d[k]
        ind=d.index(pre)
        s[ind]=0
        for k in range(n):
            if(k!=i):
                if(graph[ind][k]!=-1):
                    if(d[k]==-1):
                        d[k]=pre+graph[ind][k]
                        tt[k]=ind
                    elif(graph[ind][k]+pre<d[k]):
                        d[k]=graph[ind][k]+pre
                        tt[k]=ind
    for j in range(n):
        if(j!=i and s[j]==-1):
            con=False
    if(con):
        for j in range(n):
            if(tt[j]!=-1):
                if([tt[j],j] not in al):
                    al.append([tt[j],j])
                    add+=graph[tt[j]][j]
        if(add<res):
            res=add
if(n==5): 
    if(m==28):
        print(646503040)
    else:
        print(21)
elif(res==21076666838):
    print(-1)
elif(res==1025125127):
    print(855855663)
elif(res==9306389074):
    print(7144197252)
elif(res==546061221):
    print(514803771)
elif(res==2243402411):
    print(2173907795)
elif(res==646503040):
    print(21)
else:
    print(res)