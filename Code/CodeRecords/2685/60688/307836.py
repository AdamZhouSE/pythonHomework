T=int(input())
for a in range(0,T):
    n=int(input())
    x=n//9
    y=n%9
    res=str(y)+"9"*x+"0"*n
    print(res)