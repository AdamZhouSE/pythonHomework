def kthSmallestPrimeFraction(A, K):
        total = (len(A)-1)*len(A)/2
        left = (A[0],A[-1])
        right = (0,1)

        def findmidk(matrix, fenzi, fenmu):
            i = len(matrix) - 2
            j = 0
            res = 0
            res2 = (0,1)
            while j < len(matrix)-1 and i >= 0:
                if matrix[j]*fenmu - matrix[-i-1]*fenzi <= 0:
                    if res2[1]*matrix[j] - res2[0]*matrix[-i-1] > 0:
                        res2 = (matrix[j],matrix[-i-1])
                    res += (i + 1)
                    j += 1        
                else:
                    i -= 1
            return res,res2

        for i in range(len(A)-1):
            if right[1]*A[i] - right[0]*A[i+1] > 0:
                right = (A[i],A[i+1])
        re = left
        if K == total:
            return list(right)
        while left[0]*right[1] < right[0]*left[1]:
            fenzi = left[0]*right[1] + right[0]*left[1]
            fenmu = left[1]*right[1]*2
            num,re = findmidk(A,fenzi,fenmu)
            if num < K:
                left = (fenzi+1,fenmu)
            elif num > K:
                right = (fenzi,fenmu)
            else:
                break
        return list(re)
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
k=int(input())
ans=kthSmallestPrimeFraction(A, k)
print(ans)













