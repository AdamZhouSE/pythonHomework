import collections
t=list(map(int,input().split(' ')))
asize=t[0]
bsize=t[1]
achild=collections.defaultdict(list)
bchild=collections.defaultdict(list)
for i in range(asize-1):
    k = input().split(' ')
    a = []
    for j in k:
        if (j != ''):
            a.append(int(j))
    achild[a[0]].append(a[1])
    achild[a[1]].append(a[0])
for i in range(bsize - 1):
    k = input().split(' ')
    a=[]
    for j in k:
        if(j!=''):
            a.append(int(j))
    bchild[a[0]].append(a[1])
    bchild[a[1]].append(a[0])
v=[0 for i in range(10000)]
ares=[0 for i in range(10000)]
bres=[0 for i in range(10000)]
def dfs(x,v,child):
    c = [-1]
    for i in range(len(child[x])):
        if(v[child[x][i]]==0):
            v[child[x][i]] = 1
            c.append(dfs(child[x][i],v,child))
    return max(c)+1
for node in achild.keys():
    v = [0 for i in range(10000)]
    v[node] = 1
    ares[node]=dfs(node,v,achild)
for node in bchild.keys():
    v = [0 for i in range(10000)]
    v[node]=1
    bres[node]=dfs(node,v,bchild)
ans=0
for i in range(len(ares)):
    if(ares[i]!=0):
        for j in range(len(bres)):
            if(bres[j]!=0):
                ans+=ares[i]+bres[j]+1
print(ans)


