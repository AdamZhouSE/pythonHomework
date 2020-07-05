import sys
import re
import math
def lcm(nums):
    ceiling=1
    for a in nums:
        ceiling*=a
    big=max(nums)
    res=big
    while res<ceiling:
        isvalid=1
        for a in nums:
            if res%a!=0:
                isvalid=0
        if isvalid==0:
            res+=big
        else:
            break
    return res
def judge(a,k,m):
    if int(math.pow(2,k))*int(math.pow(3,m))>a:
        return 0
    else:
        if int(math.pow(2,k))*int(math.pow(3,m))==a:
            return 1
        else:
            return judge(a,k+1,m)+judge(a,k,m+1)+judge(a,k+1,m+1)
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
nums= [int(e) for e in digits ]
n=nums[0] 
del(nums[0])
nums=list(set(nums))
if len(nums)>10:
    print("No")
else:
    t=lcm(nums)
    times=[0]*len(nums)
    for i in range(len(nums)):
        times[i]=t//nums[i]
    isvalid=[0]*len(nums)
    for i in range(len(nums)):
        isvalid[i]=judge(times[i],0,0)
    istrue=1
    for j in isvalid:
        if j==0:
            istrue=0
            break
    if istrue==1:
        print("Yes")
    else:
        print("No")