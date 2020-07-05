t=int(input())
for i in range(t):
    n=int(input())
    a1=n*(n-1)+1
    an=n*(n+1)
    result=(a1+an)*n
    print(result)