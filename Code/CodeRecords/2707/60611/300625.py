row=eval(input())
ans = 0
for i in range(0, len(row), 2):
    x = row[i]
    if row[i+1] == x^1: continue
    ans += 1
    for j in range(i+1, len(row)):
        if row[j] == x^1:
            row[i+1], row[j] = row[j], row[i+1]
            break
print(ans)