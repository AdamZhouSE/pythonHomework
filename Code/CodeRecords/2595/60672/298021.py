def pages(n,k):
    page=1
    for i in range(n-1):
        page=page*k
    return page

T=int(input())
for i in range(T):
    string=list(input())
    N=int(string[0])
    K=int(string[-1])
    page=pages(N,K)
    print(page)