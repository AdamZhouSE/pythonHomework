n,t=map(int,input().split())
a=list(map(int,input().split()))
tmp=0
summ[0]=0
for i in range(1,n+1):
    summ[i]=sum[i-1]+a[i-1]
maxn=0
for i in range(1,n+1):
    for j in range(0,i):
        if (sum[i]-sum[j]<t) and (j-i>maxn):
            maxn=j-i
print(maxn)