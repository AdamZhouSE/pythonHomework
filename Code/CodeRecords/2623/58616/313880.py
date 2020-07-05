# LeetCode 215
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]


nums = input().split(',')
nums = [int(x) for x in nums]
k = eval(input())
s = Solution()
print(s.findKthLargest(nums, k))