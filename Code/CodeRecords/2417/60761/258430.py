nums=list(map(int,input().split(",")))
nums.sort()
ans=0
for i in range(1,len(nums)):
    if(nums[i]%nums[i-1]!=0):
        ans=1
if(ans==0):
    print(False)
else:
    print(True)