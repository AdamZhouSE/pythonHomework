str = input()
nums = str.split(",")
nums.sort()
print(nums[int(len(nums)/2)])
