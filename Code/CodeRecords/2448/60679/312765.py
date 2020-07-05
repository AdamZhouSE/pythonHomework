class Solution:
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        for i in range(len(citations)):
            if citations[i] >= n:
                return n
            n -= 1
        return 0

t = Solution()
read = input()
read = read[1:len(read) - 1]
nums = read.split(',')
nums = [int(nums[i]) for i in range(len(nums))]
print(t.hIndex(nums))
