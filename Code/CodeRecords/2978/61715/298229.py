class Solution :
    def kobe(self):
        s1 = list(raw_input())
        #print(s1)
        s2 = []
        i = 1
        while s1[i] != ' ' :
            i += 1
        del s1[i]
        while i < s1.__len__() :
            s2.append(s1[i])
            del s1[i]
        if s1 == s2 :
            return 0
        else :
            while s1[0] == s2[0] :
                del s1[0]
                del s2[0]
        return int(ord(s1[0]) - ord(s2[0]))
so = Solution()
#so.kobe()
print(so.kobe())