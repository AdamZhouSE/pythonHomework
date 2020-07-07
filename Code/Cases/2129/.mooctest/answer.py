class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if (n & 3 == 3) and (n != 3):
                n += 1
            elif n & 1 == 1:
                n -= 1
            else:
                n = n >> 1
            res += 1
        return res
a = input()
s = Solution()
print(s.integerReplacement(int(a)))