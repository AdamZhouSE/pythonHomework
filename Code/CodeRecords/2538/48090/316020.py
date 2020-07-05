arr=eval(input())



class Solution:
    def firstMissingPositive(self, nums):
        if(not nums):
            return 1
        n=len(nums)
        for i in range(n):
            while(0<nums[i]<=n and nums[i]!=nums[nums[i]-1]):
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(n):
            if(nums[i]!=i+1):
                return i+1
        return n+1



c=Solution()
print(c.firstMissingPositive(arr))