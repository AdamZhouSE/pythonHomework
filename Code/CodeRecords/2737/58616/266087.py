class Solution(object):
    def func(self, nums):
        n = len(nums)
        myDict = {}
        for x in nums:
            if x in myDict:
                myDict[x] += 1
            else:
                myDict[x] = 1
        return [x for x in myDict.keys() if myDict[x] > n/3]


x = eval(input())
s = Solution()
print(s.func(x))
