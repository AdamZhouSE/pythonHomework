nums = input().split(',')
length = len(nums)
if length == 1:
    print(str(nums[0]))
elif length == 2:
    print(str(nums[0])+"/"+str(nums[1]))
else:
    res = ''
    for i in range(0, length):
        if i == 0:
            res += str(nums[i])+"/("
        elif i == length-1:
            res += str(nums[i])+")"
        else:
            res += str(nums[i])+'/'
    print(res)