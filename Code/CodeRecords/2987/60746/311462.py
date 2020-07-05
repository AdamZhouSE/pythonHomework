A=list(input())
def newchain(N):
    n=len(N)
    nn=2*n
    new=[]
    for i in range(nn):
        new.append(0)
    for i in range(n):
        new[i]=N[i]
    for j in range(n,nn):
        new[j]=N[n-1-(j-n)]
    nstr=''.join(new)
    print(nstr)
    return 0
newchain(A)