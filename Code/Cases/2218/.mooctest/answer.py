class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.maximumProduct(c))