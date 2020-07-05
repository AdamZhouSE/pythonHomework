n=int(input())
nstr=list(input())
m=int(input())
def newstr(N,S,M):
    new=[]
    for i in range(M-1,N):
        new.append(S[i])
    nS=''.join(new)
    print(nS)
    return 0
newstr(n,nstr,m)