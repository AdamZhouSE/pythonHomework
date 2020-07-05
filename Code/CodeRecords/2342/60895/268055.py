t=int(input())
while t>0:
    t=t-1
    n,k=input().split(' ')
    N=int(n)
    K=int(k)
    s=input().split(' ')
    result=[]
    while K<=N:
        for i in range(0,K):
            result.append(s[K-1-i])
        s=s[K:]
        N=len(s)
    for j in range(0,N):
        result.append(s[N-1-j])
    for item in result:
        print(item+' ' ,end='')
    print()