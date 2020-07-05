from collections import defaultdict
def factorial(n:int)->int:
    f=1
    for i in range(1,n+1):
        f*=i
    return f

T=int(input())
for t in range(T):
    N=int(input())
    D=defaultdict(int)
    arr=list(map(int,input().split()))
    ans=0
    for i in arr:
        D[i]+=1
    for value in D.values():
        ans+=(factorial(value)//(factorial(value-2)*2))
    print(ans)