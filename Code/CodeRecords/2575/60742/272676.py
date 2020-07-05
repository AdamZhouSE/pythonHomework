s = input()
depth = 0
cur = 0
for c in s:
    if c=='(':
        cur += 1
        depth = max(depth,cur)
    else:
        cur -= 1
dpth1 = depth//2
res = [0]*len(s)
for i in range(len(s)):
    if s[i]=='(':
        cur += 1
        if cur>dpth1:
            res[i] = 1
    else:
        if cur>dpth1:
            res[i] = 1
        cur -= 1
print(res)