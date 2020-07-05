import math
class S(object):

    def num(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = A
        nums.sort()
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                if i and nums[i]==nums[i-1]:
                    continue
                if not tmp or math.sqrt(tmp[-1]+nums[i]) % 1 == 0:
                    backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return len(res)

a=input().split(",")
l=[]
for i in range(len(a)):
    l.append(int(a[i]))
s=S()
ans=s.num(l)
print(ans)