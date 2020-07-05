N, P = map(int, input().split())
keys = list(input().split())
l = []
for key in keys:
    s = key[-3:]
    pos = ((ord(s[0]) - ord('A')) * (32**2) +
           (ord(s[1]) - ord('A')) * 32 +
           (ord(s[2]) - ord('A'))) % P
    ans = pos
    if ans not in l:
        l.append(ans)
    else:
        k = 0
        while ans in l and k < P:
            k += 1
            ans = (pos + k ** 2) % P
            if ans in l:
                ans = (pos - k ** 2 + P) % P
        l.append(ans)
print(*l)

