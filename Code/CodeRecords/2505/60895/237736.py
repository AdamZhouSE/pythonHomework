class Solution(object):
    def findDuplicate(self, nums):
        for item in nums:
            if nums.count(item) != 1:
                print(item)
                return item 


    
