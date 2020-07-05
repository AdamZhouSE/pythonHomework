class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        n=len(nums)
        if(n<2):
            return n
        tail=[nums[0]]
        for i in range(1,n):
            if(nums[i]>tail[-1]):
                tail.append(nums[i])
                continue
            l=0
            r=len(tail)-1
            while(l<=r):
                mid=(l+r)//2
                if(tail[mid]>=nums[i]):
                    r=mid-1
                else:
                    l=mid+1
            tail[l]=nums[i]
        return len(tail)

