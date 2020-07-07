class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        dp=[0]*n
        for i in range(2,n):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
        return sum(dp)
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.numberOfArithmeticSlices(c))