import re
class Solution :
    def kobe(self):
        arr = str(input())
        n = re.split('\[|\]|,',arr)
        del n[0]
        del n[n.__len__()-1]
        n.sort()
        for i in range(1, n.__len__()-1) :
            if n[i] != n[i-1] and n[i+1] != n[i] :
                return n[i]
so = Solution()
print(so.kobe())