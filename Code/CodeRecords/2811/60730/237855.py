m, n = map(int, input().split())
ans = -1
b = [0] * m
for i in range(n):
    a = int(input()) % m
    if (b[a]):
        ans = i + 1
        break
    b[a] = 1

print(ans)