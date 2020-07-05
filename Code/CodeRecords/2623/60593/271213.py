a=list(map(int,input().split(',')))
k=int(input())
a.sort()
print(a[len(a)-k])