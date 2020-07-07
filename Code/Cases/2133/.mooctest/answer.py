class Solution(object):
    def minMoves(self, nums):
        sum = 0
        minmum = min(nums)
        for i in nums:
            sum += i-minmum
        return sum
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.minMoves(c))