from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy=nums[:]
        nums_copy.sort()
        left=float("inf")
        right=0
        for i in range(len(nums)):
            if(nums_copy[i]!=nums[i]):
                left=min(left,i)
                right=max(right,i)
        return right-left+1 if(right-left+1 > 0) else 0


a=eval(input())
s=Solution()
print(s.findUnsortedSubarray(a))