n = int(input())
s = input()
res = l = 0
for i in s:
    if i == 'V':
        l += 1
    elif l != 0:
        if l > 2:
            res += 2
        else:
            res += 1
        l = 0
if l > 1:
    res += 1
print(res,end='')