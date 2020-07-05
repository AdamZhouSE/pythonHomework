T = int(input())
while T > 0:
    T -= 1
    nums = input()
    res = 0
    for i in range(len(nums) - 2):
        for j in range(i + 3, len(nums) + 1):
            tmp = nums[i:j]
            dp = [0] * 3
            # print(tmp)
            for k in range(len(tmp)):
                if tmp[k] == '0':
                    dp[0] += 1
                elif tmp[k] == '1':
                    dp[1] += 1
                else:
                    dp[2] += 1
                # print(dp)
            if dp[0] == dp[1] & dp[1] == dp[2]:
                res += 1
    print(res)
