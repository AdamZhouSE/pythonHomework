import bisect
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        height = [x[1] for x in envelopes]
        dp = []
        for x in height:
            idx = bisect.bisect_left(dp,x)
            if idx == len(dp):
                dp.append(x)
            else:
                dp[idx] = x
        return len(dp)
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)

s = Solution()
print(s.maxEnvelopes(n))