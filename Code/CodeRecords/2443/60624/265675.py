def func4():
    nums = list(map(int, input()[1:-1].split(",")))
    res = ""
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if int(str(nums[i])+str(nums[j])) < int(str(nums[j])+str(nums[i])):
                nums[i], nums[j] = nums[j], nums[i]
    for x in nums:
        res += str(x)
    print(res)
    return
func4()