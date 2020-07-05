inp = int(input())
nums=input().split(" ")
for i in range(inp):
    nums[i]=int(nums[i])
res=0
for i in range(inp):
    if(nums[i]>=1):
        res+=(nums[i]-1)
    else:
        res+=(1-nums[i])
print(res)