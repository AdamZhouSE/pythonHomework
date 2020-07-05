s=[]
while True:
    try:
        ts=input()
    except:
        break

    if len(ts)!=1:
        ts=ts[1:]
        if ts[len(ts)-1]==',':
            ts=ts[:len(ts)-1]
        ts=ts[1:len(ts)-1]
        ts.replace('"','')
        l=ts.split(",")
        ls=[]
        for x in l:
            ls.append(int(x))
        s.append(ls)

forest=s

trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
sr = sc = ans = 0
for _, tr, tc in trees:
    d = dist(forest, sr, sc, tr, tc)
    if d < 0: 
        return -1
    ans += d
    sr, sc = tr, tc
print(ans)