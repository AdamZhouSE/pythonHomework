def pancakeSort(A):
        res=[]
        for i in range(len(A),1,-1):
            A = A[:A.index(i)-1]+A[:A.index(i)]
            res.append(A.index(i)+1)
            res.append(i)
        return res
A=eval(input())
a=pancakeSort(A)
while(1 in a):
    a.pop(a.index(1))
print(a)