from itertools import permutations
n=int(input())
k=int(input())
source=[]
for a in range(1,n):
    source.append(a)
target=list(permutations(source,n))
print(target)
target.sort()
print(target[k-1])