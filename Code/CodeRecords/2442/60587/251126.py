inp = input()
tmp = inp[1:len(inp) - 1].split(',')
nums = [int(tmp[i]) for i in range(len(tmp))]
if len(nums) < 2:
    print(0)
else:
    lst = list(nums)
    lst.sort()
    dp = [0] * (len(lst) - 1)
    for j in range(1, len(lst)):
        dp[j - 1] = lst[j] - lst[j - 1]
    print(max(dp))
