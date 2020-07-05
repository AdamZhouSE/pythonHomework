from itertools import combinations
sources=list(input())
lists=[]
for i in range(len(sources)):
    lists.append(i)
target=list(combinations(lists,3))
targets=[]
for i in target:
    targets.append(list(i))
count=0
for i in targets:
    if sources[i[0]]=="Q" and sources[i[1]]=="A" and sources[i[2]]=="Q":
        count=count+1
print(count,end="")