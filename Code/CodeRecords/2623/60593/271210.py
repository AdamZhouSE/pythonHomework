a=list(map(int,input().split(',')))
k=int(input())
a=sorted(a,reversed=True)
print(a[k-1])