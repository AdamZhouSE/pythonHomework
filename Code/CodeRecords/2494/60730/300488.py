m = eval(input())
ans = 0
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if m[i] > m[j] * 2:
            ans += 1
print(ans)
