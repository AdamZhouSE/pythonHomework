from collections import defaultdict
N=int(input())
tree=defaultdict(list)
for i in range(N-1):
    x,y=tuple(map(int,input().split()))
    tree[x].append(y)
    tree[y].append(x)
ans=(1,1)
def find(node:int,visited:list,depth:int,ans:tuple)->tuple:
    visited.append(node)
    flag=False
    for c in tree[node]:
        flag=False
        if c not in visited:
            ans=find(c,visited,depth+1,ans)
            flag=True
        if not flag:
            ans=max(ans,(node,depth+1),key=lambda x:x[1])
    return ans
ans=find(1,[],0,ans)
ans=find(ans[0],[],0,ans)
print(ans[1]-1)