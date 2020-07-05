def func1():
    nums = list(map(int, input().split(',')))
    res = ''
    res += str(nums[0])+'/('
    for i in range(1, len(nums)-1, 1):
        res += str(nums[i])+'/'
    res += str(nums[len(nums)-1])+')'
    print(res)
    return
func1()