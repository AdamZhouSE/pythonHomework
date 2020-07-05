T=int(input())
for t in range(T):
    line=input().split()
    A=set(input().split())
    B=set(input().split())
    N=len(A)
    ans=0
    for a in A:
        if a in B:
            ans+=1
    print(ans)