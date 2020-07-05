s = input()
t = input()
res = True
for i in range(len(s)):
    if i < len(s) - 1:
        if (not t.count(s[i])) or t.index(s[i]) >= t.index(s[i + 1]):
            res = False
            break
    else:
        if not t.count(s[i]):
            res = False
            break
print(res)