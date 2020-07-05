


def format(s):
    s = list(s)
    s[0] = ''
    s[len(s) - 1] = ''
    a = ''.join(s)
    a = a.split(",")
    i = 0
    while i < len(a):
        a[i] = int(a[i])
        i = i + 1
    return a


Res = 0
i = 0
a = input()
after = format(a)
before = after
after = sorted(after)
for num in after:
    if num == before[i]:
        Res = Res + 1
        i = i + 1
    else:
        break

for num in range(len(after)-1,-1,-1):
    if after[num] == before[num]:
        Res=Res+1
    else:
        break

print(len(after)-Res)