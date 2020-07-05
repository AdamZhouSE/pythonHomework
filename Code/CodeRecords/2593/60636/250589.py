from itertools import combinations
t=int(input())
for j in range(t):
    n=int(input())
    source=input()
    if("," in source):
        source=source.split(",")
    else:
        source=source.split(" ")
    sources=[]
    for i in source:
        sources.append(int(i))
    lists=[]
    for i in range(n):
        lists.append(i)
    target=list(combinations(lists,4))
    targets=[]
    for i in target:
        x=[]
        for a in i:
            x.append(a)
        targets.append(x)
    res=[]
    for i in targets:
        if(sources[i[0]]+sources[i[1]]==sources[i[3]]+sources[i[2]]):
            res.append(i)
    res.sort()
    if(len(res)==0):
        print("no pairs")
    else:
        print(*res[0])