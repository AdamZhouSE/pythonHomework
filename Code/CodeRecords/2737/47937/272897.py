class Solution(object):
       def majorityElement(self, nums):
           """
           :type nums: List[int]
           :rtype: List[int]
           """
           from itertools import groupby
           res = []
           n = len(nums) / 3
           for k, v in groupby(sorted(nums)):
               # print(k,len(list(v)))
               if len(list(v)) > n:
                   res.append(k)
           return res
    
a=eval(input())
#print(a)
s=Solution()

print(s.majorityElement(a))