n = int(input())
gap = list(map(int, input().split(' ')))
m, n = map(int, input().split(' '))
ans = 0
for i in range(m - 1, n - 1):
    ans += gap[i]
print(ans)
