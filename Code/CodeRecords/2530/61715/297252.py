
class Solution :
    def strSort(self):
        S = list(raw_input())
        T = list(raw_input())
        for i in range(T.__len__()) :
            ind = S.index(T[i])
            T[i] = ind
        T.sort()
        for i in range(T.__len__()):
            T[i] = S[T[i]]
        strT = "".join(T)
        print(strT)
so = Solution()
so.strSort()