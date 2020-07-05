class Solution(object):
    def func(self, numbers):
        myDict = dict()
        
        maxLen = 0
        for i in numbers:
            if i not in myDict:
                start = myDict.get(i - 1, 0)
                end = myDict.get(i + 1, 0)
                curLen = 1 + start + end
                if curLen > maxLen:
                    maxLen = curLen
                myDict[i - start] = curLen
                myDict[i + end] = curLen
                myDict[i] = curLen
        return maxLen


x = eval(input())
s = Solution()
print(s.func(x))