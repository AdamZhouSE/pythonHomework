nums=eval(input())
n=len(nums)
max_num=nums[0]
right=0
for i in range(n):
    if(nums[i]>=max_num):
        max_num=nums[i]
    else:
        right=i
left=n
min8=nums[-1]
for i in range(n-1,-1,-1):
    if(nums[i]<=min8):
        min8=nums[i]
    else:
        left=i
print(right-left+1)
