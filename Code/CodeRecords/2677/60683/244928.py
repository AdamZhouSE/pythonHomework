T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    times = 1
    res = 0
    for j in range(N - 1):
        if nums[j] == nums[j + 1]:
            times += 1
        else:
            res += times * (times - 1) // 2
            times = 1
    res += times * (times - 1) // 2
    print(res)