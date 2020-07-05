def permute(n):
    def backtrack(s, t):
        if s == t:
            res.append(''.join(n))
            return
        for i in range(s, t):
            n[i], n[s] = n[s], n[i]
            backtrack(s + 1, t)
            n[i], n[s] = n[s], n[i]

    res = []
    backtrack(0, len(n))
    return res


n = eval(input())
k = eval(input())
raw = [str(i + 1) for i in range(n)]
a = permute(raw)
print(a[k - 1])
