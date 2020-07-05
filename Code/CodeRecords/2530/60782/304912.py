"""
题目描述

字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。

S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

返回任意一种符合条件的字符串T。

输入描述

两行分别是字符串S和 T。S的最大长度为26，其中没有重复的字符。T的最大长度为200。S和T只包含小写字符。
输出描述

返回排好序的字符串T
"""


class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ""
        for s in S:
            if s in T:
                res += s * T.count(s)
        for t in T:
            if t not in S:
                res += t
        return res


s = Solution()
print(s.customSortString(input(), input()))
