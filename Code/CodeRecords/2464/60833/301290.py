from _testcapi import INT_MAX
t=int(input())
nums=list(map(int,input().split(',')))
l=0
sum=0
res=INT_MAX
for i in range(0,len(nums)):
    sum+=nums[i]
    while(sum>=t):
        res=min(res,i+1-l)
        sum-=nums[l]
        l+=1
if res!=INT_MAX:
    print(res)
else:
    print(0)
