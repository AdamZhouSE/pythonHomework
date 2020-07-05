from itertools import combinations
source=list(input())
sources=[]
for i in source:
    sources.append(int(i))
print(sources)
lists=[]
for i in range(len(sources)):
    lists.append(i)
target=list(combinations(lists,2))
print(target)
res=[]
for i in target:
    x=sources.copy()
    a=x[i[0]]
    x[i[0]]=x[i[1]]
    x[i[1]]=a
    res.append(x)
res.append(sources)
print(*max(res))