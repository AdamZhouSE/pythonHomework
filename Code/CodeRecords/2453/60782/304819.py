"""
题目描述
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
    编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
"""


class Solution:
    def search(self, nums, target):
        if len(nums) == 0: return False
        if len(nums) == 1: return nums[0] == target
        b = len(nums) - 1
        n = len(nums) // 2
        a = 0
        if nums[a] == target or nums[b] == target or nums[n] == target: return True
        while a < b and nums[a] == nums[b] == nums[n]:
            a = a + 1
            b = b - 1
            if nums[a] == target: return True
        n = (a + b + 1) // 2

        if (nums[n] >= nums[a]):
            if (nums[n] <= target or target < nums[a]):
                return self.search(nums[n:b + 1], target)
            else:
                return self.search(nums[a:n], target)

        else:
            if (nums[n] > target or nums[b] < target):
                return self.search(nums[a:n], target)
            else:
                return self.search(nums[n:b + 1], target)


s = Solution()
print(s.search(list(map(int, input().split(","))), int(input())))
