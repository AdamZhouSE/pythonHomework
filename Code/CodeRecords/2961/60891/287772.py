s = input()
s_len = len(s)
a = []
for i in range(s_len):
    a.append([])
for i in range(s_len):
    to_a = s[i:] + s[0:i]
    a[i].append(to_a)
a.sort()
ans = ''
for i in range(s_len):
    ans += a[i][0][s_len - 1]
print(ans)