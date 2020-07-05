t=int(input())
for i in range(t):
    n=int(input())
    a=input().split(' ')
    a=list(map(int,a))
    done=[False]*n
    if len(a)==1:
        print(0)
        continue
    cnt=0
    time=0
    while(cnt<n):
        m=max(a)
        i=a.index(m)
        if (i-1>=0 and a[i-1]!=0 and i+1<n and a[i+1]!=0) or (i-1<0 and a[i+1]!=0) or (i+1>n-1 and a[i-1]!=0):
            a[i]=0
        else:
            time+=m
            a[i]=-1
        cnt+=1
    print(time)