import itertools
def pro(n,k):
    c=[i for i in range(1,n+1)]
    d=list(itertools.permutations(c,4))
    print(d)


n=int(input())
k=int(input())
pro(n,k)
