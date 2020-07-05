N, S = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
for j in range(N - 1):
    re = 0
    for i in range(0, (N - j) // 2 + 1):
        if sum(a[j:j + i]) <= S and sum(a[j + i:j + 2 * i]) <= S:
            re = 2 * i
    print(re)
print(0)