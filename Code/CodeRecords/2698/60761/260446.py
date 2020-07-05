def func(d,n):#f[i]=f[i−1]N+1
    if(d==0):
        return 1
    elif(d==1):
        return 2
    else:
        return func(d-1,n)**n+1
n,d=map(int,input().split(" "))
print(func(d,n)-func(d-1,n),end="")

    