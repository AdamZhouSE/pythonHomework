nums = input().split(",")
if len(nums) == 1:
    print(nums)
else:
    result = str(nums[0])+"/("
    for i in range(1,len(nums)):
        result = result + str(nums[i])+"/"
    print(result[:-1]+")")