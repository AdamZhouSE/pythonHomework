nums = eval(input())
nums.sort()
count = len(nums)
if count<3:
    print(0)
else:
    for i in range(0,count-2):
        if nums[count-1-i]<nums[count-2-i]+nums[count-3-i]:
            print(nums[count-1-i]+nums[count-2-i]+nums[count-3-i])
            break
        elif i == count-3:
            print(0)