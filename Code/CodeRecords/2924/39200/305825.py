def cal(ai, bi, d):
    if r - ai[bi.index(min(bi))] >= d:
        return d * min(bi)
    else:
        minb = min(bi)
        d -= r - ai[bi.index(minb)]
        count = (r - ai[bi.index(minb)]) * minb
        ai.pop(bi.index(minb))
        bi.pop(bi.index(minb))
        return count + cal(ai, bi, d)
    return


str1 = input().split()
n = int(str1[0])
r = int(str1[1])
avg = int(str1[2])
ai = []
bi = []
nowsum = 0
for x in range(n):
    str2 = input().split()
    ai.append(int(str2[0]))
    nowsum += int(str2[0])
    bi.append(int(str2[1]))
needsum = avg * n
d = needsum - nowsum
if d <= 0:
    print(0)
else:
    print(cal(ai, bi, d))
