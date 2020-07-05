a=eval(input())


class Solution:
    def sortArrayByParity(self, A) :
        i=0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A

c=Solution()
print(c.sortArrayByParity(a))