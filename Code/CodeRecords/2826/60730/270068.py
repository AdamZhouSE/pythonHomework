n = int(input())
row = list(map(int, input().split()))
row = sorted(row)
num = i = 0
for i in range(n-1):
    for j in range(i+1, n):
        if row[i] == row[j]:
            num += 1
            row[j] += 1
        else:
            continue
    row = sorted(row)
print(num)
