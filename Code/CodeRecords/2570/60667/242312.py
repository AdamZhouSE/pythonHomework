import bisect
nums = int(input())
envelopes = []
for i in range(nums):
    envelopes.append(list(map(int,input().split(','))))
envelopes.sort(key = lambda x: (x[0],-x[1]))
height = [x[1] for x in envelopes]
dp = []
for x in height:
    idx = bisect.bisect_left(dp,x)
    if idx == len(dp):
        dp.append(x)
    else:
        dp[idx] = x
print(len(dp))   