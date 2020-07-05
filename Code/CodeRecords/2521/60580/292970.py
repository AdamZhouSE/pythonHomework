l = eval(input())
d = {}
for i in l:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
s = ""

tList = sorted(d.items(), key=lambda item: item[1])
keyList = []
for i in tList:
    keyList.append(i[0])
while len(s) < len(l):
    for var in keyList:
        if d[var] != 0:
            s += str(var)
            d[var] -= 1
    if len(s) == len(l) - 1:
        break
for var in keyList:
    if d[var] != 0:
        s = str(var) + s
print("[", end='')
k = 0
while k < len(s):
    if k == len(s) - 1:
        print(" " + s[k], end=']')
        print("")
    elif k == 0:
        print(s[k], end=',')
    else:
        print(" " + s[k], end=',')
    k += 1
