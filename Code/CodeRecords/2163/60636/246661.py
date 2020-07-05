from itertools import permutations
n=int(input())
k=int(input())
source=[]
for a in range(1,n):
    source.append(a)
target=list(permutations(source,n))
target.sort()
print(targer[k-1])