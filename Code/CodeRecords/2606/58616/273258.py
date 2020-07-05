class Solution:
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1


x = eval(input())
t = eval(input())
solve = Solution()
print(solve.search(x, t))
