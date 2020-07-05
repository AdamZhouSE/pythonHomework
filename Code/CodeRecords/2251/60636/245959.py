from itertools import combinations
numb=int(input())
sources=[]
for i in range(numb):
    x=input().split(",")
    source=[]
    source.append(int(x[0]))
    source.append(int(x[1]))
    sources.append(source)
target=list(combinations(sources),3)
print(target)