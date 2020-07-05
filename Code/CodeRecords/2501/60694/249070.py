n = int(input())
before = list(map(str, input().split()))
after = list(map(str, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        a, b = before[i], before[j]
        if after.index(a) > after.index(b):
            cnt += 1
print(cnt)
