import numpy
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a = numpy.linspace(0, 19, num=20)
        a = 3 ** a
        return n in a
a = input()
s = Solution()
print(s.isPowerOfThree(int(a)))