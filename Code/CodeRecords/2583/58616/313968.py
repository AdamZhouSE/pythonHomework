# LeetCode 1201
class Solution:
    def nthUglyNumber(self, n, a, b, c):
        from math import gcd
        def lcm(x,y):
            return x * y // gcd(x,y)
        def lower(x):
            lcm1 = lcm(a,b)
            lcm2 = lcm(b,c)
            lcm3 = lcm(a,c)
            lcm4 = lcm(lcm1,lcm2)
            return x // a + x // b + x // c + x // lcm4 - x // lcm1 - x // lcm2 - x // lcm3
        lo = 0
        hi = int(2e9)
        while lo != hi:
            mid = lo + hi >> 1
            if lower(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo


n = eval(input())
a = eval(input())
b = eval(input())
c = eval(input())
s = Solution()
print(s.nthUglyNumber(n, a, b, c))