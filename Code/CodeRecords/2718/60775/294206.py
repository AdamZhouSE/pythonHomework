s = input()
pos = eval(input())

sets = [pos[0]]
for x in pos:
    is_in = False
    for y in sets:
        a = x[0] in y
        b = x[1] in y
        if a or b :
            is_in = True
            if a and not b:
                y.append(x[1])
            elif not a and b:
                y.append(x[0])
            break
    if not is_in:
        sets.append(x)
allstring = []
for x in sets:
    tmp = []
    for i in x:
        tmp.append(s[i])
    tmp.sort()
    allstring.append(tmp)
    x.sort()

tmpidx = []
tmpstr = []
for x in sets:
    tmpidx.extend(x)
for x in allstring:
    tmpstr.extend(x)
result = list(s)
for i,x in enumerate(tmpidx):
    result[x] = tmpstr[i]
ss = ''.join(x for x in result)
print(ss)
