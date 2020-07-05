nums = input().split(',')
result = ""
if len(nums) == 1:
    result = nums
else:
    result = nums[0] + "/" 
    if len(nums) > 2:
        result = result + "("
    for n in range(1,len(nums)):
        result = result + nums[n] + "/" 
    result = result[:-1]
    if len(nums) > 2:
        result = result + ")"
print(result)