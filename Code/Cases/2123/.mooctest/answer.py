class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5 == int(num**0.5)
a = input()
s = Solution()
print(s.isPerfectSquare(int(a)))