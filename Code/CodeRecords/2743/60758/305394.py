n=int(input())
num=list(map(int,input().split()))
tree=[[]for i in range(n+1)]
out=[0 for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
def deep(current,target,visited):
    if current==target:
        for i in visited:
            out[i]+=1
        return
    for i in tree[current]:
        if i not in visited:
            visited.append(i)
            deep(i,target,visited.copy())
            visited=visited[0:len(visited)-1]
for i in range(0,len(num)-1):
    a=num[i]
    b=num[i+1]
    deep(a,b,[a])
for i in range(1,len(out)):
    if i!=1:
        out[i]-=1
    print(out[i])