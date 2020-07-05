import copy
temp=[int(x) for x in input().split()]
n=temp[0]
k=temp[1]
graph=[[-1]*n for i in range(n)]
for i in range(n-1):
    temp=[int(x)-1 for x in input().split()]
    x=temp[0]
    y=temp[1]
    graph[x][y]=1
    graph[y][x]=1
res=[]
def candl(graph,k):
    global n
    if(k==0):
        for i in range(n):
            f=True
            temp=copy.deepcopy(graph)
            union=[[x] for x in range(n)]
            for j in range(n):
                temp[i][j]=-1
                temp[j][i]=-1
            for m in range(n):
                for s in range(n):
                    if(temp[m][s]==1):
                        for x in union:
                            if(m in x):
                                t1=x
                            if(s in x):
                                t2=x
                        if(t1!=t2):
                            union.remove(t1)
                            union.remove(t2)
                            union.append(t1+t2)
            for x in union:
                if(len(x)>n/2):
                    f=False
                    break
            if(f and i not in res):
                res.append(i)
        return
    else:
        temp=copy.deepcopy(graph)
        for i in range(n):
            for j in range(n):
                if(temp[i][j]==1 and i!=j):
                    temp[i][j]=-1
                    temp[j][i]=-1
                    for m in range(n):
                        for s in range(n):
                            if(temp[m][s]==-1 and m!=s):
                                temp[m][s]=1
                                temp[s][m]=1
                                candl(temp,k-1)
                                temp[m][s]=-1
                                temp[s][m]=-1
                    temp[i][j]=1
                    temp[j][i]=1
candl(graph,k)
for i in range(n):
    if(i in res):
        print(1)
    else:
        print(0)
            
                                
                
            
