def func35():
    in_str = input()
    nums = list(map(int, in_str[1:-1].split(", ")))
    sorted_nums = sorted(nums)
    low = 0
    high = len(nums)-1
    while low <= high and sorted_nums[low] == nums[low]:
        low += 1
    while low <= high and sorted_nums[high] == nums[high]:
        high -= 1
    print(high - low  + 1)
    return
func35()