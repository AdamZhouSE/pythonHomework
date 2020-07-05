n=int(input())
a=list(map(int,input().split()))
idx=[a.index(min(a)),a.index(max(a))]
print(n-min(min(idx),n-1-max(idx))-1)