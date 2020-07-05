# 12
s = input()
d = 0
ok = True
for i in range(len(s)):
    if s[i] == '(':
        d += 1
    if s[i] == ')':
        d -= 1
    if d < 0:
        ok = False
        break
if ok == True and d == 0:
    print('YES',end = '')
else:
    print('NO',end = '')