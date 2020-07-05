n = int(input())
s = input().split(' ')
for i in range(n):
    s[i] = int(s[i])

sortedS = sorted(s)
ans = []
for i in range(n):
    index = s.index(sortedS[i])
    ans.append(index + 1)
    s = s[:i] + s[i:index + 1][::-1] + s[index + 1:]

for j in range(n):
    if j != n - 1:
        print(ans[j], end=' ')
    else:
        print(ans[j], end=' ')