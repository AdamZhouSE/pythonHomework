def pancakeSort(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = list()
        for i in range(len(A), 1, -1):
            A = A[:A.index(i)-1] + A[:A.index(i)]
            res += [A.index(i)+ 1, i]
            
        return res
A=eval(input())
a=pancakeSort(A)
while(1 in a):
    a.pop(a.index(1))
print(a)