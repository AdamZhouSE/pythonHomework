class Solution:
    def findErrorNums(self, nums):
        S = sum(set(nums))
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.findErrorNums(c))