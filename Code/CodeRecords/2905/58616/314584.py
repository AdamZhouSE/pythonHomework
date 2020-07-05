# LeetCode 1290
class Solution:
    def getDecimalValue(self, lst) -> int:
        bin_str = ""
        for i in lst:
            bin_str = bin_str + str(i)
        return int(bin_str, 2)


lst = eval(input())
s = Solution()
print(s.getDecimalValue(lst))