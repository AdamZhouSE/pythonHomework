def func3():
    nums = list(map(int, input()[1:-1].split(",")))
    length = len(nums)
    flag = True
    for i in range(length):
        while 0 < nums[i] <= length and nums[nums[i] - 1]!=nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(length):
        if nums[i] != i + 1:
            flag = False
            print(i + 1)
            break
    if flag:
        print(length+1)
    return
func3()