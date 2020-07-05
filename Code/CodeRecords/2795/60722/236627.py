n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
nums=list(set(nums))
nums.sort()
if len(nums)==1:
    result=0
elif len(nums)==2:
    result=nums[1]-nums[0]
    if result%2==0:
        result=result//2
elif len(nums)==3 and (nums[1] - nums[0]) == (nums[2] - nums[1]):
        result = nums[1] - nums[0]
else:
    result = -1
print(result)