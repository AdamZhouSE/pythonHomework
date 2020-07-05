T=int(input())
for a in range(0,T):
    n=int(input())
    if(n==1):
        print(3)
    elif(n==2):
        print(8)
    else:
        res=2*n+1+n*(n-1)+n*(n-1)//2+n*(n-1)*(n-2)//2
        print(res)