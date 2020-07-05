from itertools import combinations
arr=input().split(',')
k,n=int(arr[0]),int(arr[1])
result=[]
if k==1:
    result.append([[n]])
else:
    nums=[1,2,3,4,5,6,7,8,9]
    for i in combinations(nums,k):
        if sum(i)==n:
            result.append(list(i))
print(result)
