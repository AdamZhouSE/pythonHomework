"""
题目描述
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 先找到两个第二个升序数组的第一项的
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pol = l
        ans = self.binary_search(target, nums[:pol])
        if ans == -1:
            ans = self.binary_search(target, nums[pol:])
            if ans != -1:
                ans += len(nums[:pol])

        return ans

    # 二分查找index值函数
    def binary_search(self, target, nums):
        index = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index = mid
                break
        return index


s = Solution()
print(s.search(list(map(int, input().split(","))), int(input())))
