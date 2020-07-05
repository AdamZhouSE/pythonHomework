alist=list(map(int,input().split(',')))
K=int(input())
gap=max(alist)-min(alist)
print(0 if gap<2*K else gap-2*K)