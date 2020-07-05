n = int(input())
s = input()
ss = s
ans = 0
flag = 0

for i in range(0, n - 1):
    if ss[i] == 'V' and ss[i + 1] == 'K':
        ans += 1
        tmp = ss[0:i] + 'v' + ss[i + 1:n]
        ss = tmp
        tmp = ss[0:i + 1] + 'k' + ss[i + 2:n]
        ss = tmp
        # ss[i + 1] = 'k'
for i in range(0, n - 1):
    if s[i + 1] == s[i]:
        ans += 1
        flag = 1
        print(ans)
        break
if flag == 0:
    print(ans)
