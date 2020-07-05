initial=list(input())
ST=int(input())
def ToNum(N,S):
    n=len(N)
    new=[]
    for i in range(0,n-1):
        a=S+ord(N[i])-97
        new.append(a)
    return new
def fate(N,S):
    new=ToNum(N,S)
    nn=len(new)
    t=nn+1
    for i in range(nn):
        t=t-1
        for j in range(t-1):
            new[j]=new[j]+new[j+1]
    return new[0]
print(ToNum(initial,ST))
print(fate(initial,ST))