from itertools import permutations
n=int(input())
k=int(input())
source=[]
for a in range(1,n+1):
    source.append(a)
target=list(permutations(source,n))
target.sort()
print(target[k-1])