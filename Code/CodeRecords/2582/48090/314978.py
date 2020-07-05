x=input()
y=input()
xlist=x.split(",")
ylist=y.split(",")
xlist=[int(xlist[i])for i in range(len(xlist))]
ylist=[int(ylist[i])for i in range(len(ylist))]

class Solution:
    def maxAbsValExpr(self, arr1, arr2):

        n=len(arr1)
        d=[[],[],[],[]]
        b=[[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in range(n):
            for j in range(4):
                d[j]+=[arr1[i]+b[j][0]*arr2[i]+b[j][1]*i]
        return max([max(d[i])-min(d[i]) for i in range(4)])

c=Solution()
print(c.maxAbsValExpr(xlist,ylist))