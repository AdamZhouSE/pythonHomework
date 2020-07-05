s = input()
K = 0
while s != '':
    n = len(s)
    d = {}
    for j in range(n):
        for l in range(j + 1, n + 1):
            temp = s[j:l]
            if temp in d.keys():
                d[temp] += 1
            else:
                d[temp] = 1
    mlen = 0
    s = ''
    for i, j in d.items():
        if j > 1 and len(i) > mlen:
            mlen = len(i)
            s = i
    K += 1
print(K)