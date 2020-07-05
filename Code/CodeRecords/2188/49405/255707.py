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

def dp(n, a, length, k):
    ans = 0
    sum = 0
    e = 0
    for i in range(n):
        if a[i] > e:
            ans += 1
            sum += a[i]
            e = a[i] + length - 1
    return ans, sum

def work(s, t, k):
    mat = kmp(s, t)
    return dp(len(mat), mat, len(t), k)

n, k = map(int, input().split())
a = input()
b = input()
q = int(input())
for i in range(q):
    s, t, l, r = map(int, input().split())
    ans, sum = work(a[s - 1:t], b[l - 1:r], k)
    print(k * ans - sum - (s - 1) * ans)