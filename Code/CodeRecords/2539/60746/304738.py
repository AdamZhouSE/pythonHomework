def shortest(A):
    n=len(A)
    left=0
    right=n-1
    best=n
    for j in range(1,n):
        if A[j]>=A[j-1]:
            pass
        else:
            a=j-1
            break
    for s in range(n-2,a,-1):
        for t in range(s,a,-1):
            if A[t]<=A[t+1]:
                    pass
            else:
                b=t+1
                break
    if b-a+1<best:
        best=b-a+1
    return best

A=[2,6,4,8,10,9,15]
print(shortest(A))