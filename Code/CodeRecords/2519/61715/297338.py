
class Solution :
    def maxPerimeter(self):
        A = list(input())
        A.sort()
        i = A.__len__()-1
        if (A.__len__() < 3) :
            return 0
        while i > 1 :
            if A[i] >= A[i-1] + A[i-2] :
                del A[i]
            else :
                break
            i -= 1
        if (A.__len__() < 3) :
            return 0
        return A[i] + A[i-1] + A[i-2]
so = Solution()
print(so.maxPerimeter())