T=int(input())
for i in range(0,T):
    N=int(input())
    a=list(map(int,input().split()))
    for m in range(0,N-1):
        for n in range(0,N-1):
            if a[n]%2==1 and a[n+1]%2==0:
                tmp=a[n]
                a[n]=a[n+1]
                a[n+1]=tmp
    for k in a:
        print(k,end=' ')
    print()