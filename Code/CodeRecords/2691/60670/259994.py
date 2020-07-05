t=int(input())
for tt in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    sum_1=0
    for num in a:
        sum_1+=num
    sum_2=sum_1//2
    f=[[0 for i in range(0,sum_2+1)] for i in range n]
    used=[False for i in range(0,n)]
    for i in range(0,n):
        for j in range(0,sum_2+1):
            f[i][j]=f[i-1][j]
            if j-a[i]>=0:
                f[i][j]=max(f[i][j],f[i-1][j-a[i]]+a[i])
    print(sum_1-2*f[n-1][sum_2])