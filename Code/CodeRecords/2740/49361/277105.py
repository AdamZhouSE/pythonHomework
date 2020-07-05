class Solution:
    def findMinDifference(self, timePoints):
        n = len(timePoints)
        res = []
        for i in range(n):
            res.append(int(timePoints[i][0:2]) * 60 + int(timePoints[i][3:5]))
        res.sort()
        tmp = res[0] + 24 * 60 - res[n - 1]
        for i in range(1, n):
            tmp = min(tmp, res[i] - res[i - 1])
        return tmp


inputStr = input().strip()
var = inputStr.replace("[", "").replace("]", "").split(",")
result = []
for item in var:
    result.append(item.replace('"', ''))
s = Solution()
print(s.findMinDifference(result))