if __name__ == '__main__':
    s = input().strip('[]').split('], [')
    d = {}
    for i in range(len(s)):
        t = s[i].split(', ')
        if t[0] not in d.keys():
            d[t[0]] = t[1]
        else:
            if t[1]<d[t[0]]:
                d[t[0]] = t[1]
    res = []
    cur = 'JFK'
    while len(d)!=0:
        pre = cur
        res.append(cur)
        cur = d[cur]
        del d[pre]
    res.append(cur)
    print(res)

