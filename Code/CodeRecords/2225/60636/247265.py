from itertools import combinations_with_replacement as cwr
n=int(input())
m=int(input())
print(n)
print(m)
sources=[]
for i in range(n):
    sources.append(i)
target=list(cwr(sources,r=m))
print(target)