def my_count(s1, s2):
    n = len(s2)
    ct = 0
    for i in range(len(s1)-n+1):
        sub = s1[i:i+n]
        if sub==s2:
            ct += 1
    return ct


t = int(input())
while t:
    cmd = input().split( )
    k = int(cmd[1])
    s = cmd[0]
    n = len(s)
    ct = [0] * n
    subs = [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)]
    subs = list(set(subs))
    for sub in subs:
        if my_count(s, sub) == k:
            ct[len(sub) - 1] += 1
    ct.reverse()
    ans = n-ct.index(max(ct))
    ans = -1 if max(ct) == 0 else ans
    print(ans)
    t -= 1
