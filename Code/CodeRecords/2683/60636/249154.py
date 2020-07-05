from itertools import combinations
t=int(input())
for i in range(t):
    source=list(input())
    lists=[]
    for j in range(len(source)):
        lists.append(j)
    targets=[]
    for a in range(1,len(source)):
        target=list(combinations(lists,a))
        for j in target:
            targets.append(j)
    lengths=[]
    for j in targets:
        if(sorted(j)==j):
            length.append(len(j))
    print(max(lengths))