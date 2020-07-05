from collections import defaultdict

nums=eval(input())


class Solution:
    def sortArray(self, nums):

        def counter_sort(nums,key=lambda x:x):
            B,C = [], defaultdict(list)
            for x in nums:
                C[key(x)].append(x)
            for k in range(min(C), max(C) + 1):
                B.extend(C[k])
            return B
        res = counter_sort(nums)
        return res


c=Solution()
print(c.sortArray(nums))