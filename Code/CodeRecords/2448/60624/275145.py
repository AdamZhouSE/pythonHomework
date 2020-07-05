def func6():
    nums = list(map(int,input()[1:-1].split(",")))
    nums.sort()
    for i in range(len(nums)):
        h = len(nums)-i
        if h <= nums[i]:
            print(h)
            break
    return
func6()