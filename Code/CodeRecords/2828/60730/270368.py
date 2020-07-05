n = int(input())
row = list(map(int, input().split()))
num = row[0]
tmp = 0
for i in range(n - 1):
    if tmp - row[i + 1] + row[i] >= 0:
        tmp = tmp - row[i + 1] + row[i]
        continue
    else:
        num = row[i + 1] - row[i] - tmp + num
        tmp = 0
print(num)
