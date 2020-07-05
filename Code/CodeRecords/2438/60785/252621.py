nums= input("")
str=nums[1:len(nums)-1]
nums = list(map(int, str.split(",")))
print(sorted(nums))
