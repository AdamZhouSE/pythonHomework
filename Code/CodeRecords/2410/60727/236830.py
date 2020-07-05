class Solution(object):
    def longestSubsequence(self, arr, difference):
        n = len(arr)
        d = {}
        for i in range(n):
            d[arr[i]] = d.get(int(arr[i]) - difference, 0) + 1
        return max(d.values())



arr = input().split(",")
difference = int(input())
s = Solution()
print(s.longestSubsequence(arr,difference ))