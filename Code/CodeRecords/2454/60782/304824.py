"""
题目描述
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    你可以假设数组中不存在重复元素。
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) / 2
        while (left <= right):
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            mid = left + (right - left) / 2
        return -1


s = Solution()
print(s.search(list(map(int, input().split(",")))))
