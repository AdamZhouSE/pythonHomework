def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n,m=map(int,input().split(" "))
ans=int(factorial(n*m)/(factorial(m*n-n+1)*factorial(n-1)*n))
print(ans%10007)