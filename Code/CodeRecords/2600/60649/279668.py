n=int(input())
a=list(map(int,input().split()))
t=list(map(int,input().split()))
#t数组代表被删的顺序，t[0]即第一个被删的
time=1
for _ in range(n):
    a[t[_]-1]=-1
    sum1,maxsum=0,0
    for i in range(n):
        if a[i]==-1:
            maxsum=max(maxsum,sum1)
            sum1=0
        else:
            sum1+=a[i]
    maxsum=max(maxsum,sum1)
    print(maxsum)
