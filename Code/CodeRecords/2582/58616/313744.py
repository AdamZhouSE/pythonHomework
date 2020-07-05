# LeetCode 1131
class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        n=len(arr1)
        d=[[],[],[],[]]
        b=[[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in range(n):
            for j in range(4):
                d[j]+=[arr1[i]+b[j][0]*arr2[i]+b[j][1]*i]
        return max([max(d[i])-min(d[i]) for i in range(4)])


arr1 = input().split(',')
arr1 = [int(x) for x in arr1]
arr2 = input().split(',')
arr2 = [int(x) for x in arr2]
s = Solution()
print(s.maxAbsValExpr(arr1, arr2))