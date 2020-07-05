#全排列暴力算法
import itertools
res=[]
n=int(input())
k=int(input())
a=''.join(str(i) for i in list(range(1,n+1)))
for i in itertools.permutations(a,n):
    res.append(''.join(str(j) for j in i))
print(res[k-1])    
