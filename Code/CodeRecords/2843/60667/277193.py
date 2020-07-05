n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n-1):
    b.append(a[i]+a[i+1])
b.append(a[-1])
r = ''
for i in range(n):
    r += str(b[i])
    if i < n - 1:
        r += ' '
print(r)