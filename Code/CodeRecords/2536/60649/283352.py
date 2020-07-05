import collections
tic=eval(input())
d=collections.defaultdict(list)
for fr,to in tic:
    d[fr]+=[to]
for f in d:
    d[f].sort()
res=[]
def dfs(f):
    while d[f]:
        dfs(d[f].pop(0))
    res.insert(0,f)
dfs('JFK')
print(res)