class Solution:
    def divide(self, divd: int, dior: int) -> int:
        res = 0
        sign =  1 if divd ^ dior >= 0 else -1
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            res += 1
            divd -= dior
        res = res*sign
        return min(max(-2**31, res), 2**31-1)
a = input()
b = input()
s = Solution()
print(s.divide(int(a), int(b)))