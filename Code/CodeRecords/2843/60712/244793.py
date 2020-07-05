n = int(input())
a = list(map(int,input().split()))
b = [0]*n
for i in range(n):
    if i!=n-1:
        b[i]=a[i]+a[i+1]
    else:
        b[i]=a[i]
print(*b)