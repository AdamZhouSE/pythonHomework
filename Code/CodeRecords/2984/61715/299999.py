class Solution :
    def kobe(self):
        s1 = raw_input()
        s2 = raw_input()
        if s1.__len__() != s2.__len__() :
            return 1
        if s1 == s2 :
            return 2
        s1 = s1.upper()
        s2 = s2.upper()
        if s1 == s2 :
            return 3
        return 4
so = Solution()
print(so.kobe())