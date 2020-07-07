class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            if "0" in str(i):
                continue
            for num in str(i):
                if i % int(num) != 0:
                    break;
            else:
                result.append(i)
        return result
a = input()
b = input()
s = Solution()
print(s.selfDividingNumbers(int(a), int(b)))