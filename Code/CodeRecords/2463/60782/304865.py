"""
题目描述
    给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
    说明:
        返回的下标值（index1 和 index2）不是从零开始的。
        你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
"""


class Solution(object):
    def BiSearch(self, numbers, target):
        # 通过二分法寻找每个差值的下标mid
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == numbers[mid]:
                return mid
            elif target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(numbers)
        for i in range(nums_len):
            dif = target - numbers[i]
            # 在numbers[i+1:]中获取差值下标
            dif_index = self.BiSearch(numbers[i + 1:], dif)
            if dif_index != -1:
                return [i + 1, dif_index + i + 2]
        return []


s = Solution()
print(s.twoSum(list(map(int, input().split(","))), int(input())))
