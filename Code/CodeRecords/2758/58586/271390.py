def factorial(start,num):
    mul=start
    for i in range(start+1,num+1):
        mul*=i
    return mul
n,m=map(int,input().split(" "))
res=(factorial(n,n*m)//factorial(1,m*n-n+1)//n)%10007
print(res)