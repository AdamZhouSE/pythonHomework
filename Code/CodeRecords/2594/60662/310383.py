t = int(input())
res = []
for i in range(t):
    s = list(str(input()).upper())
    flag = 0
    length = []
    for j in range(0, len(s) - 1):
        if s.count(s[j]) > 1:
            d = 0
            h = len(s) - 1
            while h > j:
                if s[h] == s[j]:
                    d = h - j - 1
                    length.append(d)
                    break
                h -= 1
    if len(length)>0:
        res.append(max(length))
    else:
        res.append(-1)

for i in res:
    print(i)