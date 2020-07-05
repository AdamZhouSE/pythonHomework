from itertools import combinations
k,n=map(int,input().split(','))
nums=[1,2,3,4,5,6,7,8,9]
res=[]
for i in range(len(nums)):
    res+=list(combinations(nums,i))
res=[x for x in res if len(x)==k]
a=[]
for j in res:
    if(sum(j)==n):
        a.append(list(j))
print(a)

