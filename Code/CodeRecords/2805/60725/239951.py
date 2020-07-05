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

作者：zhu_shi_fu
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-zhu-xing-jie-shi-python3-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。