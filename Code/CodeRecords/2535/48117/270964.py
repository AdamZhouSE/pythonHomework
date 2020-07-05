s = input()[1:-1].split(',')
for i in range(len(s)):
    s[i] = int(s[i])

ans = 0
max_ = 0
for i, x in enumerate(s):
    max_ = max(max_, x)
    if max_ == i:
        ans += 1

print(ans)

