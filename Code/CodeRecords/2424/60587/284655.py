T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    dp = [0] * int(n)
    for i in range(0, len(num)):
        for j in range(0, len(num)):
            if num[i] == num[j]:
                dp[i] += 1
    res = 0
    for i in range(0, len(num)):
        if dp[i] % 2 != 0:
            res = num[i]
            break
    print(res)
