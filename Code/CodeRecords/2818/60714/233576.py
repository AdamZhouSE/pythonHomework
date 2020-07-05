n, x = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]
time.sort()
ans = 0
for i in range(0, n):
    if x > 1:
        ans += x * time[i]
        x -= 1
    else:
        ans += x * time[i]
print(ans)
