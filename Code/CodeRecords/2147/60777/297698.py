temp=[int(x) for x in input().split(' ')]
n=temp[0]
m=temp[1]
k=temp[2]-1
a=temp[3]
b=temp[4]
dis=[[-1]*n for i in range(n)]
for i in range(m):
    temp=[int(x)-1 for x in input().split(' ')]
    x=temp[0]
    y=temp[1]
    dis[y][x]=a
    dis[x][y]=a
    
best=[[-1]*n for i in range(n)]
for i in range(n):
    pre=[-1]*n
    al=[]
    for j in range(n):
        if(dis[i][j]!=-1):
            pre[j]=dis[i][j]
    for k1 in range(n-1):
        now=max(pre)
        ind=pre.index(now)
        for j in range(n):
            if(pre[j]!=-1 and pre[j]<=now and j not in al):
                now=pre[j]
                ind=j
        al.append(ind)
        for j in range(n):
            if(j!=i):
                if(pre[j]==-1 and dis[ind][j]!=-1):
                    pre[j]=dis[ind][j]+now
                elif(dis[ind][j]!=-1 and dis[ind][j]+now<pre[j]):
                    pre[j]=dis[ind][j]+now
    best[i]=pre
node=[]    
for i in range(n):
    for j in range(i+1,n):
        if(best[i][j]==2*a):
            node.append([i,j])
        
for x in node:
    i=x[0]
    j=x[1]
    if(dis[i][j]>b or dis[i][j]==-1):
        dis[i][j]=b
pre=[-1]*n
al=[]
ind
for j in range(n):
        if(dis[k][j]!=-1):
            pre[j]=dis[k][j]
for k1 in range(n-1):
        now=max(pre)
        ind=0
        for j in range(n):
            if(pre[j]!=-1 and pre[j]<now and j not in al):
                now=pre[j]
                ind=j
        al.append(j)
        for j in range(n):
            if(pre[j]==-1 and dis[ind][j]!=-1):
                pre[j]=dis[ind][j]+now
            elif(dis[ind][j]!=-1 and dis[ind][j]+now<pre[j]):
                pre[j]=dis[ind][j]+now
for i in range(len(pre)):
    if(i==k):
        print(0)
    else:
        print(pre[i])