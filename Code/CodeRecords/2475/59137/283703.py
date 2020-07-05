def s28():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(input().split())
        for j in range(n):
            nums[j] = int(nums[j])

        nums = sorted(nums)
        ans = 0
        now = 0

        for j in range(n):
            if now == 0:
                now = 1
            elif nums[j] - nums[j-1] == 1:
                now += 1
            else:
                if now > ans:
                    ans = now
                now = 1
        if now > ans:
            ans = now

        print(ans)


s28()