class Solution(object):
    def func(self, nums):
        n = len(nums)
        myDict = dict()
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        return [i for i in myDict.keys() if myDict[i] > n/3]


x = eval(input())
s = Solution()
print(s.func(x))
