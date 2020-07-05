from itertools import permutations
n=int(input())
k=int(input())
res=list(permutations(list(range(1,n+1)), n))[k-1]
s=""
for i in res:
    s=s+str(i)
print(s)