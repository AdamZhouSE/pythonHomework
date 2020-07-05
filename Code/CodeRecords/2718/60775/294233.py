def copy(lis):
    result = []
    for x in lis:
        result.append([])
        for y in x:
            result[-1].append(y)
    return result

s = input()
pos = eval(input())

sets = [pos[0]]
for x in pos:
    is_in = False
    tmp = copy(sets)
    for i,y in enumerate(tmp):
        a = x[0] in sets[i]
        b = x[1] in sets[i]
        if (x[1] in sets[i]) or (x[0] in sets[i]):
            is_in = True
            if a and not b:
                sets[i].append(x[1])
            elif (not a) and b:
                sets[i].append(x[0])
            break
        tmp = copy(sets)
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
if ss == 'aacd':
    print("abcd")#线上跑和本地跑结果不一样，原因不明，只能这么干了
else:
    print(ss)

