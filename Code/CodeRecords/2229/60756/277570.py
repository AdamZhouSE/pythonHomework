def isReserved(A:list)->bool:
    p=0
    n=0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            p+=1
            n+=1
        for j in range(i + 2, len(A)):
            if A[j] < A[i]:
                n+=1
    return n==p

A=list(map(int,input().split(",")))
print(isReserved(A))