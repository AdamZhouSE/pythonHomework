"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
"""
import collections


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([char * freq for char, freq in collections.Counter(s).most_common()])


s = Solution()
print(s.frequencySort(input()))
