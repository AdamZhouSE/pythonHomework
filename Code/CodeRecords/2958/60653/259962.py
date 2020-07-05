s = input()
ss = list(s)
slen = len(s)
n = 103
num = [0]*n
for i in range(1, 10):
    num[i] = 1
for i in range(10, 100):
    num[i] = 2
num[100] = 3
f = [[999999]*(slen+2) for i in range(0, (slen+2))]
for i in range(0, slen):
    f[i][i] = 1
for l in range(2, slen+1):
    for i in range(0, slen):
        j = i + l - 1
        if j >= slen:
            break
        for k in range(i, slen):
            f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j])
        for k in range(i, slen):
            len = k - i + 1
            if l % len == 0:
                flag = True
                for q in range(i, j+1):
                    if ss[q] != ss[(q-i)%len+i]:
                        flag = False
                        break
                if flag:
                    f[i][j] = min(f[i][j], 2 + f[i][k] + num[int(l / len)])
print(f[0][slen-1])