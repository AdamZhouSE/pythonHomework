import math
class Solution:
    def pathInZigZagTree(self, label: int):
        n = math.floor(math.log2(label))
        if n%2 == 1:
            label = 2**(n+1)+2**n-1-label
        res = [label]
        while res[0] != 1:
            res.insert(0,math.floor(res[0]/2))
            #print(res)
        for i in range(1,len(res),2):
            res[i] = 2**(i+1)+2**i-1-res[i]
        return res
a = int(input())
s = Solution()
print(s.pathInZigZagTree(a))