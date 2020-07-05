def findmax(a):
    j=0
    num=a[0]
    for i in range(1,len(a)):
        if a[i]>num:
            num=a[i]
            j=i
    return j
def pancakeSort(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = list()
        for i in range(len(A), 1, -1):
            index = findmax(A[:i])
            A = A[:index][::-1] + A[index:]
            A = A[:i][::-1]
            res += [index, i]
        return res
print(pancakeSort([3,2,4,1]))