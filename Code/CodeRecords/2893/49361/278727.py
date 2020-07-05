from collections import Counter


class Solution:
    def singleNumber(self, nums):
        hashmap = Counter(nums)

        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k
nums = input()
print(Solution().singleNumber(nums))