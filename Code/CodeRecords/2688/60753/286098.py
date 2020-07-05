import sys
import re
def findsubset(isUsed,arr,indx,count,n):
    k=len(arr)
    if indx==k:
        ans=[]
        for i in range(k):
            if isUsed[i]==1:
                ans.append(arr[i])
        if sum(ans)==n:
            count.append(1)
    else:
        isUsed[indx]=0
        findsubset(isUsed,arr,indx+1,count,n)
        isUsed[indx]=1
        findsubset(isUsed,arr,indx+1,count,n)        
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    k=nums[0]
    del(nums[0])
    lists=[0]*k
    for j in range(k):
        lists[j]=nums[0]
        del(nums[0])
    n=nums[0]
    del(nums[0])
    count=[]
    isUsed=[0]*k
    findsubset(isUsed,lists,0,count,n)
    print(len(count))
    