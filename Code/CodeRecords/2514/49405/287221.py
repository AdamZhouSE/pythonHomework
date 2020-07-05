def kmp(s, t):
    n, m = map(len, (s, t))
    nxt = [0 for i in range(m)]
    mat = []
    j = 0
    for i in range(1, m):
        while j > 0 and t[i] != t[j]: j = nxt[j - 1]
        if t[i] == t[j]: j += 1
        nxt[i] = j
    j = 0
    for i in range(n):
        while j > 0 and s[i] != t[j]: j = nxt[j - 1]
        if s[i] == t[j]: j += 1
        if j == m:
            mat.append(i - m + 1 + 1)
            j = nxt[j - 1]
    return mat

s = input()
t = input()
print(len(kmp(s, t)) > 0)