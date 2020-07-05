def longest(A):
    n=len(A)
    m=min(A)
    M=max(A)
    a=m
    b=M
    best=0
    for k in range(0,n):
        i=A[k]
        for j in range(i+1,i+n):
            if j in A:
                b=j
                t=b-a+1
                if t>best:
                    best=t
            else:
                break
    return best

A=[100,4,200,1,3,2]
print(longest(A))
           