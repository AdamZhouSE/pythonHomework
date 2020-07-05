def s36():

    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    def solve(last, day, nums):
        day = day + 1
        if day >= len(nums):
            return 0
        today = nums[day]

        if last == 0:
            if today == 0:
                return 1 + solve(0, day, nums)
            elif today == 3:
                return min(solve(1, day, nums), solve(2, day, nums))
            else:
                return solve(today, day, nums)
        else:
            if today == 0 or today == last:
                return 1 + solve(0, day, nums)
            else:
                return solve(3-last, day, nums)
        return 0

    count = solve(0, -1, nums)
    print(count)


s36()