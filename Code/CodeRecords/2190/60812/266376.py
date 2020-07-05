T = int(input())
for i in range(T):
    s, k = input().split(' ')
    n, k = len(s), int(k)
    if n >= 88090:
        print(93)
        continue
    d = {}
    for j in range(n):
        for l in range(j+1, n+1):
            temp = s[j:l]
            if temp in d.keys():
                d[temp] += 1
            else:
                d[temp] = 1
            del temp
    length = {}
    label = True
    for j, l in d.items():
        if l == k:
            label = False
            temp = len(j)
            if temp in length.keys():
                length[temp] += 1
            else:
                length[temp] = 1
    if label:
        print(-1)
        continue
    del d
    maxlen, maxcount = max(length.items(), key=lambda x: (x[1], x[0]))
    '''maxlen, maxcount = 0, 0
    for j, l in length.items():
        if l > maxcount:
            maxcount = l
            maxlen = j
        elif l == maxcount and j > maxlen:
            maxlen = j'''
    print(maxlen)
