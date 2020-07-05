n,m,k,a,b=map(int,input().split(" "))
graph=[]
def findmin(l,jud):
    min=10000
    mini=0
    for i in range(0,n):
        if jud[i]:
            continue
        if l[i]<min:
            min=l[i]
            mini=i
    return mini
def shortcut(start):
    temp=graph.copy()
    jud=[]
    res=(temp[start])[:]
    for j in range(0,n):
        jud.append(False)
    for j in range(0,n):
        m=findmin(res,jud)
        jud[m]=True
        for k in range(0,n):
            if temp[m][k]+res[m]<res[k]:
                res[k]=temp[m][k]+res[m]
    return res
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        if i==j:
            temp.append(0)
        else:
            temp.append(10000)
    graph.append(temp)
for i in range(0,m):
    t1,t2=map(int,input().split(" "))
    graph[t1-1][t2-1]=a
    graph[t2-1][t1-1]=a
shortlist=[]
if 2*a>b:
    for i in range(0,n):
        minlist=shortcut(i)
        shortlist.append(minlist)
    for i in range(0,n):
        for j in range(0,n):
            if shortlist[i][j]==2*a:
                graph[i][j]=b
res=shortcut(k-1)
for item in res:
    print(item)