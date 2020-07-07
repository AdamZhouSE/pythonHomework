class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))
a = input()
s = Solution()
print(s.isPowerOfTwo(int(a)))