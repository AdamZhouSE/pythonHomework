T=int(input())
for i in range(0,T):
    N=int(input())
    a=list(map(int,input().split()))
    l=[]
    for j in range(0,N-1):
        if a[j]>=max(a[j+1:N]):
            l.append(a[j])
    l.append(a[N-1])
    print(' '.join(str(s) for s in l))