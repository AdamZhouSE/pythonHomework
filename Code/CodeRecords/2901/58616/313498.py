# LeetCode 693
class Solution(object):
    def hasAlternatingBits(self, n):
        return not ('11' in str(bin(n)) or '00' in str(bin(n)))

n = eval(input())
s = Solution()
if s.hasAlternatingBits(n):
    print("True")
else:
    print("False")