from itertools import product
def pro(n,k):
    c=[i for i in range(1,n+1)]
    d=list(product(c,n))
    print(d)


n=int(input())
k=int(input())
combinate(n,k)
