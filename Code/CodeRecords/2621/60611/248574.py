nums = list(map(int,input().split(",")))
length=len(nums)
result=nums[0]
max=-1000000000
for i in range(1,length):
    if result+nums[i]<nums[i]:
        result=nums[i]
    else:
        result=result+nums[i]
    if max<result:
        max=result
print(max)