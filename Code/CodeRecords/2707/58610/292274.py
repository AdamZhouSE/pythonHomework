row = eval(input())
ans = 0
for i in range(len(row)):
    while row[i ^ 1] != row[i] ^ 1:
        tar = row[i ^ 1] ^ 1
        for j in range(i + 1, len(row)):
            if row[j] == tar:
                row[j], row[i] = row[i], row[j]
                ans += 1
                break
print(ans)