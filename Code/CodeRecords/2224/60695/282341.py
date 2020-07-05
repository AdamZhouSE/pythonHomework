n = input()
m = sorted(n)
m.reverse()
m = "".join(m)

if n == m:
    print(n)
else:
    m = 0
    mindex = 0
    s = 10
    sindex = 0
    for i in range(0, len(n)):
        if int(n[i]) > m:
            m = int(n[i])
            mindex = i
        if int(n[i]) < s:
            s = int(n[i])
            sindex = i
    if mindex < sindex:
        if mindex == 0:
            result = n[sindex]+n[mindex + 1:sindex] + n[mindex] + n[sindex + 1:]
        else:
            result = n[0:mindex] + n[sindex] + n[mindex + 1:sindex] + n[mindex] + n[sindex + 1:]
    else:
        if sindex == 0:
            result = n[mindex] + n[sindex + 1:mindex] + n[sindex] + n[mindex + 1:]
        result = n[0:sindex] + n[mindex] + n[sindex + 1:mindex] + n[sindex] + n[mindex + 1:]
    print(result)