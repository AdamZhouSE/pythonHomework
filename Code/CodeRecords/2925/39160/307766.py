n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.reverse()
d = {}
for i in range(n):
    d[b[i]] = i
    
ans = 0
m = 0
last = d[a[0]]
for i in range(1, n):
    if d[a[i]] > last:
        ans += 1
    last = min(d[a[i]], last)

print(ans)