def func19():
    nums = list(map(int, input().split(",")))
    if len(nums) <= 2:
        print(0)
    else:
        res = 0
        add = 0
        for i in range(2, len(nums)):
            if nums[i-1]-nums[i] == nums[i-2]-nums[i-1]:
                add += 1
                res += add
            else:
                add = 0
        print(res)
    return
func19()