a=int(input())
b=int(input())
c=int(input())

class Solution:
    def n(self, a, b, c):
        dmin, dmid, dmax = sorted([abs(a - b), abs(a - c), abs(b - c)])
        return [0 if dmid == 1 else (dmin > 2) + 1, dmax - 2]

s=Solution()
res=s.n(a,b,c)
print(res)