s=input()
k=int(input())
res, m, maxl = 0, collections.Counter(), 0
for i in range(len(s)):
    m[s[i]] += 1
    maxl = max(maxl, m[s[i]])
    if res - maxl < k:
        res += 1
    else:
        m[s[i - res]] -= 1
print(res)