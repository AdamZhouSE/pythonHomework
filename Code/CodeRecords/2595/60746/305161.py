def pages(N,K):
    sum=0
    page=[]
    t=1
    page.append(t)
    for i in range(1,N):
        t=t*K
        page.append(t)
    for i in range(0,N):
        sum=sum+page[i]
    return sum

def outputpages(T,N,K):
    for i in range(0,T):
        n=N[i]
        k=K[i]
        print(pages(n,k))
    return 0
T=3
N=[5,2,3]
K=[2,3,4]
outputpages(T,N,K)