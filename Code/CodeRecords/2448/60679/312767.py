class Solution:
    def hIndex(self, nums):
        nums.sort()
        h = len(nums)
        for i in range(len(nums)):
            if nums[i] >= h:
                return h
            h -= 1
        return 0

t = Solution()
read = input()
read = read[1:len(read) - 1]
nums = read.split(',')
nums = [int(nums[i]) for i in range(len(nums))]
print(t.hIndex(nums))
