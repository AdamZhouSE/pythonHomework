from itertools import combinations
get_input=input()
k=get_input[0]
n=get_input[1]
nums=[1,2,3,4,5,6,7,8,9]
res=[]
for i in range(0,len(nums)):
    res+=list(combinations(nums,i))
res=[x for x in res if len(x)==k]
a=[]
for j in res:
    if sum(j)==n:
        a.append(list(j))
print(a)