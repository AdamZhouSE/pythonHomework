def s1():
    nums = list(eval(input()))
    count = 0
    for i in range(0, len(nums), 2):
        if nums[i] % 2 == 0 and nums[i+1] - nums[i] == 1:
            pass
        elif nums[i] % 2 == 1 and nums[i] - nums[i+1] == 1:
            pass
        elif nums[i] % 2 == 0:
            target = nums[i] + 1
            index = nums.index(target)
            nums[i+1], nums[index] = nums[index], nums[i+1]
            count += 1
        else:
            target = nums[i] - 1
            index = nums.index(target)
            nums[i+1], nums[index] = nums[index], numd[i+1]
            count += 1
    print(count)


s1()