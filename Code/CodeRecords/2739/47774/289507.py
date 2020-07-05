from itertools import combinations
k,n=eval(input())
output=[]
res=[]
nums=[1,2,3,4,5,6,7,8,9]
for i in nums:
    res +=list(combinations(nums,i))
res=[x for x in res if len(x) == k]
for i in res:
    if sum(i) ==n :
        output.append(list(i))
print(output)