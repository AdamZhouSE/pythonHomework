sb=input()
nums=list(map(int,input().split()))
res=0
for i in range(len(nums)):
    if(nums[i]%2==0):
        res+=nums[i]
        nums[i]=-1
nums.sort()
while(nums[0]==-1):
    nums.remove(-1)
if(len(nums)%2==1):
    nums.pop(0)
for i in nums:
    res+=i
print(res)