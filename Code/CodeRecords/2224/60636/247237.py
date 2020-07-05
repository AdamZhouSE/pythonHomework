from itertools import combinations
source=list(input())
sources=[]
for i in source:
    sources.append(int(i))
lists=[]
for i in range(len(sources)):
    lists.append(i)
target=list(combinations(lists,2))
res=[]
for i in target:
    x=sources.copy()
    a=x[i[0]]
    x[i[0]]=x[i[1]]
    x[i[1]]=a
    res.append(x)
res.append(sources)
ans=""
for i in max(res):
    ans=ans+str(i)
print(ans)