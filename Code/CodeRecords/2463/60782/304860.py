"""
题目描述
    给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
    说明:
        返回的下标值（index1 和 index2）不是从零开始的。
        你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        li = []
        for i in range(len(numbers)):
            if numbers[i] in dic.keys():
                # 将原始值和差值的下标分别添加到li中
                li.append(dic[numbers[i]] + 1)  # 原始值的下标
                li.append(i + 1)  # 差值的下标
                return li

            # 将每个值的差值及对应的下标, 保存在字典中
            dic[target - numbers[i]] = i

        return None


s = Solution()
print(s.twoSum(list(map(int, input().split(", "))), int(input())))
