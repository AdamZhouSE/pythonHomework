n = int(input())

index = sorted(map(int, input().split()))
p, v = 0, 0
for i in index:
    v += max(0, p - i + 1)
    p = max(p + 1, i)
print(v)
