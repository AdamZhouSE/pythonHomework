n = int(input())
s = input()
ans = 0
flag = 0
for i in range(0, n - 1):
    if s[i] == 'V' and s[i + 1] == 'K':
        ans += 1
        s[i:i + 1] = 'v'
        s[i + 1:i + 2] = 'k'
for i in range(0, n - 1):
    if s[i + 1] == s[i]:
        ans += 1
        flag = 1
        print(ans)
        break
if flag == 0:
    print(ans)
