T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    l=list(map(int,input().split()))
    res=[]
    for j in range(N-K+1):
        tmp=l[j:j+K]
        tmp.sort()
        res.append(tmp[-1])
    for k in range(N-K+1):
        print(res[k],end=" ")
    print()
