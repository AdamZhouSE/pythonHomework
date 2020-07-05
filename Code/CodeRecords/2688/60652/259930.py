def f(n,a):
    ans=0
    if n==0:
        return 1
    for i in range(0,len(a)):
        ans+=f(n-a[i],a[i+1:])
    return ans


T=int(input())
for sample in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    print(f(m,a))