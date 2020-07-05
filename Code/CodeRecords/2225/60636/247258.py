from itertools import combinations_with_replacement as cwr
n=int(input())
m=int(input())
sources=[]
for i in range(n):
    sources.append(i)
target=lists(cwr(sources,m))
print(target)