def func13():
    nums = list(map(int, input()[1:-1].split(",")))
    print([num for num in set(nums) if nums.count(num)>len(nums)/3])
    return
func13()