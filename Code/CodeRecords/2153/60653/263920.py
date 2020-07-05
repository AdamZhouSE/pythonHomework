s = input()
n = int(s)
s = list(s)
ans = []
flag = True
if n > 0:
    s.reverse()
#    print("".join(str(n) for n in s))
elif n == 0:
    flag = False
    print('0', end='')
else:
    ans.append('-')
    s.reverse()
    s.pop()
boo = False
for i in s:
    if i != '0':
        ans.append(i)
        boo = True
    elif i == '0' and boo:
        ans.append(i)
print("".join(str(n) for n in ans))