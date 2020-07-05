class Solution :
    def kobe(self):
        s1 = list(raw_input())
        s2 = ''
        s1.append(' ')
        int1 = [0]
        for i in range(s1.__len__()-1) :
            if s1[i] == ' ' :
                int1.append(0)
            else :
                int1[-1] += 1
        maxlength = 0
        maxindex = 0
        targetlength = 0
        for i in range(int1.__len__()) :
            if maxlength < int1[i] :
                maxlength = int1[i]
                maxindex = i
        for i in range(maxindex) :
            targetlength += int1[i] + 1
        while s1[targetlength] != ' ' :
            s2 += s1[targetlength]
            targetlength += 1
        print(s2)
so = Solution()
so.kobe()