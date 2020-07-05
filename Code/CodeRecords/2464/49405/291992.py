t = int(input())
a = list(map(int, input().split(",")))
n = len(a)
ans = 9999
for i in range(n):
    for j in range(i, n):
        if sum(a[i:j + 1]) >= t:
            ans = min(j - i + 1, ans)
print(ans)