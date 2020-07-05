def fun(n):
    if(n==1 or n==2 or n==3):
        return 1
    else:
        return fun(n-2)+fun(n-3)
t=int(input())
for i in range(0,t):
    k=int(input())
    print(fun(k+1))