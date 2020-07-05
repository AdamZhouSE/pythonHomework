lis = eval(input())

nums = [i for i in lis]
nums.sort()
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        print(nums[i])
        break
