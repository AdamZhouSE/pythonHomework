def getSumK():
    x=input().split()
    N=int(x[0])
    K=int(x[1])
    arr=list(map(int,input().split()))
    ans=float("-Inf")
    for i in range(N-K+1):
        s=sum(arr[i:i+K])
        ans=max(ans,s)
    return ans

T=int(input())
for t in range(T):
    print(getSumK())