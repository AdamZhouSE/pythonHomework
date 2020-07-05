# LeetCode 1227
class Solution:
    def nthPersonGetsNthSeat(self, n):
        return [.5, 1.][n == 1]


n = eval(input())
s = Solution()
print("{:.5f}".format(s.nthPersonGetsNthSeat(n)))