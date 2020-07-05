
n = int(input())
ans = 0
s = input()
for i in range(n - 1):
    if s[i] == 'V' and s[i + 1] == 'K':
        ans += 1
        s[i] = 'v'
        s[i + 1] = 'k'
for j in range(n - 1):
    if s[j] == s[j + 1]:
        ans += 1
        print(ans)
