class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        lookup[0] = -1
        # print(lookup)
        summing = 0
        n = len(nums)
        if n < 2 : return False
        for i in range(0,n):
            summing += nums[i]
            if k!= 0:summing %= k
            pre = lookup.get(summing,None)
            # print(lookup)
            if pre != None:
                if i - pre > 1:
                    return True
            else:
                lookup[summing] = i
        return False
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = input()
s = Solution()
print(s.checkSubarraySum(c,int(a)))