class Solution:
    def containsNearbyDuplicate(self,nums, k, t):
        if len(nums) == 0:
            return "false"
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[j]>=nums[i]and nums[j]-nums[i]<=t)or(nums[i]>nums[j]and nums[i]-nums[j]<=t):
                    if (j-i <= k) or (i - j >= -k):
                        return "true"
        return "false"
    
s = Solution()
read = input()
k = int(read[read.find("k = ")+4:read.find(", t")])
t = int(read[read.find("t = ")+4:len(read)])
read = read[read.find("[")+1:read.find("],")]
arr = read.split(",")
arr = [int(arr[i]) for i in range(len(arr))]
print(s.containsNearbyDuplicate(arr, k, t))