class Solution:
    def missingNumber(self, nums) -> int:
        return 0 if nums == [] else ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)
a = input().split(',')
b = []
for i in a:
    b.append(int(i))
s= Solution()
print(s.missingNumber(b))