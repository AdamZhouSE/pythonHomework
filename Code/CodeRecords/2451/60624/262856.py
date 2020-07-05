def func5():
    nums = list(map(int, input().split(",")))
    target = int(input())
    if target in nums:
        print(nums.index(target))
    else:
        nums.append(target)
        nums.sort()
        print(nums.index(target))
    return
func5()