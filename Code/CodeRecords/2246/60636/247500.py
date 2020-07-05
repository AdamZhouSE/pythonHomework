from itertools import permutations
source=list(input())
sources=[]
for i in source:
    sources.append(int(i))
target=list(permutations(sources,len(sources)))
targets=[]
for i in target:
    x=[]
    for a in i:
        x.append(a)
    targets.append(x)
print(targets)