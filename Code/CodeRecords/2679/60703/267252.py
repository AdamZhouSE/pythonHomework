T = int(input())
for m in range(T):
    n = int(input())
    if(n==1):
        print(3)
    elif n==2:
        print(8)
    else:
        res = (1+n+n+n*(n-1)//2+n*(n-1)+n*(n-1)*(n-2)//2)
        print(res)