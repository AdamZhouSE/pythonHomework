res=[]
def findMax(nums,calcu):
    if len(nums)==2:
        res.append(calcu)
    i=1
    while i<len(nums)-1:
        temp=nums[0:i]+nums[i+1:]
        findMax(temp,calcu+nums[i-1]*nums[i]*nums[i+1])
        i=i+1
nums=list(map(int,input().split(",")))
nums.append(1)
nums.reverse()
nums.append(1)

findMax(nums,0)
res.sort()
print(res[-1])