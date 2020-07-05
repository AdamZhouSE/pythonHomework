


def solve():
    nums = list(map(int,input().split(',')))
    res = 0

    if len(nums) < 3:
        print(0)
        return
    i = 0
    while i < len(nums) - 2:
        d = nums[i + 1] - nums[i]
        length = 2
        for j in range(i + 2,len(nums)):
            if nums[j] - nums[j - 1] == d:
                length += 1
            else:
                break
        res += (length - 2) * (length - 1) / 2
        if length == 2:
            i += 1
        else:
            i += length - 1

    print(int(res))

solve()


