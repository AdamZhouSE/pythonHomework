T=int(input())
for t in range(T):
    n=int(input())
    if n==1:
        print(3)
    elif n==2:
        print(8)
    else:
        res=1+2*n+int(n*(n-1)/2)*3+int((n-1)*(n-2)/2)*n
        print(res)