# LeetCode 1276
class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        s = (4 * cheeseSlices - tomatoSlices) / 2
        b = (tomatoSlices - 2 * cheeseSlices) / 2
        if s >= 0 and b >= 0 and s == int(s) and b == int(b):
            return [int(b), int(s)]
        return []


t = eval(input())
c = eval(input())
s = Solution()
print(s.numOfBurgers(t, c))