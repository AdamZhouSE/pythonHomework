def f(A):
    leng=len(A)
    B=[0]*leng
    i=0
    m=leng-1
    n=0
    while i<leng:
        if int(A[i])%2==1:
            B[m]=int(A[i])
            m=m-1
        if int(A[i])%2==0:
            B[n]=int(A[i])
            n=n+1
        i=i+1
    return B

M=input()
M=list(M)
print(f(M))