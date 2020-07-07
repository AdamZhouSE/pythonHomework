class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        index=len(nums)//2
        ans=0
        for i in nums:
            ans+=abs(i-nums[index])
        return ans
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.minMoves2(c))