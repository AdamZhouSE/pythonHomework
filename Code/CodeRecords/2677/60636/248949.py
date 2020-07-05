from itertools import combinations
t=int(input())
for i in range(t):
    n=int(input())
    source=input().split(" ")
    sources=[]
    for j in source:
        sources.append(int(source))
    lists=[]
    for j in range(n):
        lists.append(j)
    target=list(combinations(lists,2))
    res=0
    for j in target:
        if(sources[j[0]]==sources[j[1]]):
            res=res+1
    print(res)