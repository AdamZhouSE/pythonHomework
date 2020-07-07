class Solution(object):
    def checkPerfectNumber(self, num):
        return True if num in [6, 28, 496, 8128, 33550336] else False
a = input()
s = Solution()
print(s.checkPerfectNumber(int(a)))