def A(n,m):
    result=1
    if(m==0):
        result=1
    else:
        for i in range(n-m+1,n+1):
            result=result*i
    return result

num=int(input())
for i in range(0,num):
    n=int(input())
    m=n-n//2
    result=2**n
    for j in range(0,m+1):
        result=result-int(A(n-j+1,j)/A(j,j))
    print(result)