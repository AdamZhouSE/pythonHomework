nums = input().split(',')
k =int(input())
for i in range(0,len(nums)):
    nums[i]=int(nums[i])
    
big = max(nums)
min = min(nums)
result=0
if (big-min)<2*k:
    result =0
else:
    result =big-min-2*k
    
print(result)
