class Solution :
    def freSort(self):
        s1 = raw_input()
        s2 = list(s1)
        s2.sort()
        s3 = list(s2)     #无重复字符
        s4 = [1]    #字符个数记录
        i = 1
        while i < s3.__len__() :
            if (s3[i] == s3[i-1]) :
                del s3[i]
            else :
                i += 1
        for i in range(1, s2.__len__()) :
            if (s2[i] != s2[i-1]) :
                s4.append(1)
            else :
                s4[-1] += 1
        for i in range(s4.__len__()-1) :
            for o in range(i+1, s4.__len__()) :
                if s4[i] < s4[o] :
                    s4[i], s4[o] = s4[o], s4[i]
                    s3[i], s3[o] = s3[o], s3[i]
        i = s3.__len__()-1
        while i >= 0 :
            for o in range(s4[i]-1) :
                s3.insert(i, s3[i])
            i -= 1
        result = "".join(s3)
        print(result)
        #print(s3, s4)
so = Solution()
so.freSort()