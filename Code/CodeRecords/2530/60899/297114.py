s = input()
t = input()
m = ""
n = ""
ans = ""
for x in t:
    if x in s:
        m += x
    else:
        n += x
for i in range(len(s)):
    if s[i] in t:
        num = t.count(s[i])
        ans += s[i]*num
ans += n
print(ans)