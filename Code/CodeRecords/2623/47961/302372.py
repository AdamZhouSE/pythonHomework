a=[int(i) for i in input().split(',')]
a.sort()
b=int(input())
print(a[len(a)-b])