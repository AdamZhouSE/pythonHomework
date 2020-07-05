from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        a,b=map(Counter,(nums1,nums2))
        return list((a&b).elements())
a=eval(input())
a=[int(x) for x in a]
b=eval(input())
b=[int(x) for x in b]
t=Solution()
print(t.intersect(a,b))