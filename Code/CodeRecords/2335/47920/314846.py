class Solution(object):
    def brokenCalc(self, X, Y):
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y /= 2

        return ans + X-Y

x =int(input())
y = int(input())
s = Solution()
print(int(s.brokenCalc(x,y)))