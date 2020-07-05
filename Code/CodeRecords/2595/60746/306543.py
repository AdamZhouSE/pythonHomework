A=int(input())
new=[]
New=[]
for i in range(A):
    new.append(list(input()))
    nn=len(new[i])
    for j in range(nn):
        if new[i][j].isdecimal():
            New.append(int(new[i][j]))
nn=len(New)
N=[]
K=[]
for i in range(nn):
    if (i%2)==0:
        N.append(New[i])
    else:
        K.append(New[i])

def pages(N,K):
    page=K**(N-1)
    return page

def outputpages(T,N,K):
    for i in range(0,T):
        n=N[i]
        k=K[i]
        print(pages(n,k))
    return 0
outputpages(A,N,K)