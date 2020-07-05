# worth thinking
T=int(input())
for i in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    output=0
    if N==1:
        output=arr[0]
    else:
        a=arr[0]
        b=arr[1]
        for j in range(2,N):
            c=arr[j]+min(a,b)
            a=b
            b=c
        output=min(a,b)
    print(output)        