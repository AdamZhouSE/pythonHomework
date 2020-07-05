import sys
import re
def findsubstr(isUsed,arr,indx,increase,n):
    k=len(arr)
    if indx==k:
        ans=[]
        for i in range(k):
            if isUsed[i]==1:
                ans.append(arr[i])
        isincrease=1
        if len(ans)==0:
            isincrease=0
        else:
            for i in range(len(ans)-1):
                if ans[i]>=ans[i+1]:
                    isincrease=0
                    break
        if isincrease==1:
            increase.append(len(ans))                
    else:
        isUsed[indx]=0
        findsubstr(isUsed,arr,indx+1,increase,n)
        isUsed[indx]=1
        findsubstr(isUsed,arr,indx+1,increase,n)        
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
strs=s.split("\n")
del(strs[0])
for i in range(T):
    s1=strs[i]
    list1=list(s1)
    n=len(list1)
    isUsed=[0]*n
    increase=[]
    findsubstr(isUsed,list1,0,increase,n)
    maxlen=max(increase)
    print(maxlen)