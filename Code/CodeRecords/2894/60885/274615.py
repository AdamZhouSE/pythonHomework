l = int(input())
line = input()
getV = False
single = False
ans = 0
if line[0] == 'K':
    line = line[1:]
for c in line:
    if c == 'V':
        if getV:
            single = True
        else:
            getV = True
    elif c == 'K':
        if getV:
            ans += 1
            getV = False
        else:
            single = True
if single:
    ans += 1
print(ans,end='')