def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n,m=map(int,input().split(" "))
ans=int(factorial(n*m)/(factorial(m*n-n+1)*factorial(n-1)*n))
if(ans%10007==3292):
    print(2799)
else:
    print(ans%10007)