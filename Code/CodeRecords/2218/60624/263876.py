def func2():
    nums = list(map(int, input().split(',')))
    nums.sort()
    print(max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1]))
    return
func2()