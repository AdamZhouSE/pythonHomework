class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N)
        left = right = -1
        res = 0
        for i,c in enumerate(s):
            if c == '1' and left == -1:
                left = i
            elif c == '1' and right == -1:
                right = i
                res = max(res,right-left)
                left = i
                right = -1
        return res
a = int(input())
s = Solution()
print(s.binaryGap(a))
