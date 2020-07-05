def pre(s):
    return ord(s) - ord('A')

for t in range(int(input())):
    s = list(map(pre, sorted(list(input()), reverse=True)))
    n = len(s)
    ans = []
    ad = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = s[j] - s[i]
            if d == 0: continue
            l = 2
            a = [i, j]
            for k in range(j + 1, n):
                if s[k] == l * d + s[i]:
                    l += 1
                    a.append(k)
            if l > len(ans):
                ans = a[:]
    for c in ans:
        print(chr(s[c] + ord("A")), end="")
    print()