n = int(input())
a = sorted(map(int, input().split()))
e = False
for i in range(2, n):
    if a[i-2] + a[i-1] > a[i]:
        e = True
        break
print("YES" if e else "NO")
