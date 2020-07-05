def func6():
    nums = list(map(int, input()[1:-1].split(",")))
    nums.sort()
    if len(nums) < 2:
        print(0)
    else:
        Max = 0
        for i in range(0,len(nums)-1):
            if abs(nums[i]-nums[i+1]) > Max:
                Max = abs(nums[i]-nums[i+1])
        print(Max)
    return
func6()