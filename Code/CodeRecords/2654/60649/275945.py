N=int(input())
l=[0 for _ in range(100000)]
maxi=0
for _ in range(N):
    ai,bi,hi=map(int,input().split())
    maxi=max(maxi,bi)
    for i in range(ai,bi):
        if hi>l[i]:
            l[i]=hi
print(sum(l[0:maxi]))