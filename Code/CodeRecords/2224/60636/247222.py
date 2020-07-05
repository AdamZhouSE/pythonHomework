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