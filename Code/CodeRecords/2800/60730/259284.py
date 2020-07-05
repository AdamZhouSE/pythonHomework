num, m = map(int, input().split())
n = list(map(int, input().split()))
tmp = 0
for i in range(num - 1):
    while True:
        if n[i] >= n[i + 1]:
            n[i + 1] = n[i + 1] + m
            tmp = tmp + 1
        else:
            break
print(tmp)
