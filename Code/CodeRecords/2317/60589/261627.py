from itertools import combinations

a=input().split(',')
a=list(map(int,a))
subsets=[]
for i in range(1,len(a)+1):
    subsets.extend(list(combinations(a,i)))
ans=0
for sub in subsets:
    ans+=max(sub)-min(sub)
print(ans)