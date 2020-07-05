import collections
a=eval(input())
d=collections.defaultdict(list)
for f,t in a:
    d[f]+=[t]
for f in d:
    d[f].sort()
ans=[]
def dfs(f):
    while d[f]:
        dfs(d[f].pop(0))
    ans.insert(0,f)
dfs('JFK')
print(ans)