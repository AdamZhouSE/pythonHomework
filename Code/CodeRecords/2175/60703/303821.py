#4
def addEdge(x,y):
    global cnt
    cnt+=1
    edge[cnt]=[x,y,last[x]]
    last[x]=cnt

def dfs(cur,parent):
    tot[cur]=1
    i = last[cur]
    while i!=0:
        to = edge[i][1]
        if(to!=parent):
            dfs(to,cur)
            tot[cur]+=tot[to]
        i=edge[i][2]

def bt(x,fa,start):
    global a
    length = tot[x]
    for i in range(start,length):
        if(a[i][0]<a[start][0]):
            a[start],a[i]=a[i],a[start]
        elif(a[i][0]==a[start][0] and a[i][1]<a[start][1]):
            a[start],a[i]=a[i],a[start]
    now = a[start][2]
    sx,sy = a[start][0],a[start][1]
    a=a[:start+1]+sorted(a[start+1:],key=lambda x:(x[0]-sx,x[1]-sy))
    l =1
    k = last[x]
    while k!=0:
        y = edge[k][1]
        if(y!=fa):
            uu = bt(y,x,start+l)
            l+=tot[y]
            ans.append((now,uu))
        k = edge[k][2]
    return now

n = int(input())
edge = [[0,0,0] for i in range(2*n)]
last = [0 for i in range(n+1)]
tot = [0 for i in range(n)]
a = [[0,0,0] for i in range(n)]
cnt=0
ans = []
for i in range(n-1):
    x,y =[int(x) for x in input().split()]
    addEdge(x,y)
    addEdge(y,x)
for i in range(n):
    a[i]=[int(x) for x in input().split()]+[i]
dfs(0,-1)  
bt(0,-1,0)
ans.sort(key=lambda x:(x[0],-x[1]))
for i,j in ans:
    print(i,j)