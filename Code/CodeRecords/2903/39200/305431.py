import itertools
string = input()[1:-1].split(",")
strs = []
for x in string:
    strs.append(x[1:-1])
maxnum = 0
for x in range(len(strs)):
    resultstr = ""
    for y in range(x, len(strs)):
        flag = 0
        for z in strs[y]:
            if z in resultstr:
                flag = 1
        if flag:
            break
        else:
            resultstr += strs[y]
    if len(resultstr) > maxnum:
        maxnum = len(resultstr)
print(maxnum)
