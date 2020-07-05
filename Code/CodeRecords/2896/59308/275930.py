s1 = ''.join(input().split(' '))
s2 = ''.join(input().split(' '))
d = dict()
flag = 'NO'
for i in s2:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in s1:
    if i in d:
        d[i] -= 1
        if d[i] == 0:
            d.pop(i)
    if len(d) == 0:
        flag = 'YES'
        break
print(flag, end='')

