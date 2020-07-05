n=int(input())
list1=list(map(int,input().split(' ')))
dict={}
for i in range(1,n+1):
    dict[i]=list1[i-1]
res=100000000000000


def dfs(i, dict, visited,origin):
    if i ==origin and len(visited)!=0:
        return 0
    elif i in visited:
        return 1000000000000000000
    else:
        visited.add(i)
        return 1+dfs(dict[i],dict,visited,origin)


for i in range(1,n+1):
    if dfs(i,dict,set(),i)>0:
        res=min(res,dfs(i,dict,set(),i))
print(res)