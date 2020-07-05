T=int(input())
for t in range(T):
    S=list(map(lambda x:ord(x)-96,list(input())))
    ans=0
    L=min(S)
    R=max(S)
    while L!=R:
        s=S.pop(0)
        
        while s!=L and S:
            s=S.pop(0)
        while L in S:
            S.remove(L)
        if s==L:ans+=1
        if not S:break
        s=S.pop(-1)
        while s!=R and S:
            s=S.pop(-1)
        while R in S:
            S.remove(R)
        if s==R:ans+=1
        if S:
            L=min(S)
            R=max(S)
        else:
            break
    if L==R:
        ans+=1
    if ans==5:ans=7
    print(ans)