n = int(input())
ans = 0
for i in range(1, n + 1):
    t = int(i ** 0.5)
    if t * t == i:
        ans += 1
print(ans)