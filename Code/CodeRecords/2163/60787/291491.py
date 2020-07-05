import itertools
n=int(input())
k=int(input())
a=[int(i) for i in range(1,n+1)]
re=list(itertools.permutations(a))
print("".join([str(i) for i in re[k-1]]))