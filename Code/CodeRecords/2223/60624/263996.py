def func4():
    nums = list(map(int, input().split(',')))
    the_sum = sum(set(nums))
    n = len(nums)
    res = [sum(nums)-the_sum, n*(n+1)//2-the_sum]
    print(res)
    return
func4()