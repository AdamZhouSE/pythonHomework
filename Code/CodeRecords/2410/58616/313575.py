# LeetCode 1218
class Solution:
    def longestSubsequence(self, arr, difference):
        d = {}
        for a in arr:
            d[a] = d.get(a - difference, 0) + 1
        return max(d.values())


arr = input().split(',')
arr = [int(x) for x in arr]
difference = eval(input())
s = Solution()
print(s.longestSubsequence(arr, difference))