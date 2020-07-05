n=int(input())
k=int(input())
a=list(range(1,n+1))
a=list(map(str,a))

from itertools import permutations
p=list(permutations(a,n))

ans=[]
for e in p:
    ans.append(int(''.join(e)))
ans.sort()
print(ans[k-1])