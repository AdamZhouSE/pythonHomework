from collections import defaultdict

n=int(input())
dic=defaultdict(list)
paths=[]
for i in range(n-1):
    uv=input().split(' ')
    u=int(uv[0])
    v=int(uv[1])
    dic[u].append(v)
    dic[v].append(u)


def dfs(this,before,path):
    neighbors=dic[this][:]
    if before is not None:
        neighbors.remove(before)
    if len(neighbors)==0:
        paths.append(path)
        return
    for neighbor in neighbors:
        temp=path[:]
        temp.append(neighbor)
        dfs(neighbor,this,temp)


dfs(1,None,[1,])
paths.sort(key=lambda x:len(x))
q=paths[-1][-1]
paths=[]
dfs(q,None,[q,])
paths.sort(key=lambda x:len(x))
print(len(paths[-1])-1)