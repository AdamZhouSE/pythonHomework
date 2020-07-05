from itertools import combinations
def combinate(n,k):
    c=[i for i in range(1,n+1)]
    d=list(combinations(c,n))
    d.sort()
    print(d[k-1])


n=int(input())
k=int(input())
combinate(n,k)
