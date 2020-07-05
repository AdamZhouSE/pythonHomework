def minWindow(s, t):

    ts = set(t)
    tcnt = {}
    for tt in t:
        tv = tcnt.setdefault(tt, 0)
        tcnt[tt] = tv + 1
    pos = {}
    matchpos = {}
    minp0 = 0
    minp1 = len(s)
    scnt = {}

    for p, c in enumerate(s):
        if c in ts:
            sv = scnt.setdefault(c, 0)
            scnt[c] = sv + 1
            pos[(c, sv)] = p
            if scnt[c] >= tcnt[c]:
                matchpos[c] = pos[(c, sv + 1 - tcnt[c])]
            if len(matchpos) == len(ts):
                p0 = min([v for k, v in matchpos.items()])
                if p - p0 < minp1 - minp0:
                    minp1, minp0 = p, p0
    if len(matchpos) == len(ts):
        return s[minp0:minp1 + 1]
    return ""
testnum=int(input())
for z in range(testnum):
    s=input()
    t=input()
    ans=minWindow(s,t)
    if(ans==""):
        print(-1)
    else:
        print(ans)