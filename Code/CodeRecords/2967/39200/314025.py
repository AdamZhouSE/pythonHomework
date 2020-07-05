n = int(input())
ss = []
for x in range(n):
    ss.append(input())
ps = ss[0]
maxlength = 0
for i in range(len(ps)):
    for j in range(i + 1, len(ps) + 1):
        if j - i < maxlength:
            continue
        cs = ps[i:j]
        flag = 1
        for x in ss:
            if cs not in x:
                flag = 0
                break
        if flag:
            maxlength = max(maxlength, j - i)
print(maxlength)
