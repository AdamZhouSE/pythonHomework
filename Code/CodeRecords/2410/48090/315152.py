a=input()
b=int(input())
alist=a.split(",")
alist=[int(alist[i])for i in range(len(alist))]

class Solution:
    def longestSub(self, arr, difference) :
        d = {}
        for a in arr:
            d[a] = d.get(a - difference, 0) + 1
        return max(d.values())

c=Solution()
print(c.longestSub(alist,b))