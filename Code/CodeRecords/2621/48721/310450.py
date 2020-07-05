
class Solution:
    def max(self, nums):
        if not nums:return 
        for i in range(1, len(nums)):
            if nums[i - 1] + nums[i] > nums[i]:
                nums[i] += nums[i - 1]
        return max(nums)

    
s=input().split(",")
list1=[]
for i in range(len(s)):
    a=int(s[i])
    list1.append(a)
f=Solution()
res=f.max(list1)
print(res)
