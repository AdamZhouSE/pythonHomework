"""
题目描述
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。

    注意数组中可能存在重复的元素。
        输入: [1,3,5]
        输出: 1
        示例 2：

        输入: [2,2,2,0,1]
        输出: 0

    说明：
        这道题是 寻找旋转排序数组中的最小值 的延伸题目。
        允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for i in nums:
            ans = min(ans, i)
        return ans


s = Solution()
print(list(map(int, input().split(","))))
