a=list(map(int,input().split(',')))
k=int(input())
a.sort(reversed=True)
print(a[k-1])