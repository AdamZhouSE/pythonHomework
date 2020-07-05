from typing import List


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        from bisect import bisect_left,bisect_right,insort
        if not nums or upper<lower:
            return 0
        p = [0]
        for a in nums:
            p.append(p[-1]+a)
        n = len(p)
        self.ans = 0
        def mergesort(A):
            if len(A)<=1:
                return A
            mid = len(A)>>1
            B,C = mergesort(A[:mid]),mergesort(A[mid:])
            n = len(C)
            l = r = 0
            for b in B:
                lo,hi = b+lower,b+upper
                while l<n and C[l]<lo:
                    l += 1
                while r<n and C[r]<=hi:
                    r += 1
                self.ans += r-l
            res = []
            i = j = 0
            while i<mid:
                while j<n and C[j]<B[i]:
                    res.append(C[j])
                    j += 1
                res.append(B[i])
                i += 1
            while j<n:
                res.append(C[j])
                j += 1
            return res
        mergesort(p)
        return self.ans



t=Solution()
nums=[]
s=input()
for c in s[1:len(s)-1].split(','):
    nums.append(int(c))
print(t.countRangeSum(nums,int(input()),int(input())))