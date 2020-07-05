nums = [int(n) for n in input().split(',')]
i = 1
if nums[0] > nums[1]:
    print(0)
else:
    while i < len(nums)-1:
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            print(i)
            break
        i += 1
if i == len(nums)-1 and nums[i]>nums[i-1]:
    print(i)