def pancakeSort(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = list()
        for i in range(len(A), 1, -1):
            idx = A.index(i)
            A = A[:idx:-1] + A[:idx]
            res += [idx + 1, i]
            
        return res
A=eval(input())
a=pancakeSort(A)
while(1 in a):
    a.pop(a.index(1))
print(a)