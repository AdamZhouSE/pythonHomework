t = int(input())
for i in range(0, t):
    n, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    ans = sum(nums[: k])
    temp = ans
    for j in range(0, n - k):
        temp = temp - nums[j] + nums[j + k]
        if temp > ans:
            ans = temp
    print(ans)
