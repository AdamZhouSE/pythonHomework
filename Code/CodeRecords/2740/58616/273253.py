class Solution:
    def findMinDifference(self, timePoints):
        timePoints.sort()
        timePoints.append(timePoints[0])
        ans = 23*60 + 59
        for i in range(len(timePoints) - 1):
            a, b = timePoints[i].split(':')
            c, d = timePoints[i + 1].split(':')
            diff = abs((int(c) - int(a))*60 + int(d) - int(b))
            if diff > 720:
                diff = 1440 - diff
            ans = min(ans, diff)
        return ans


time = eval(input())
solve = Solution()
print(solve.findMinDifference(time))
