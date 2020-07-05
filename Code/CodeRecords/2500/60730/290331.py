m = eval(input())
length, res = len(m), []
i = length
while i > 1:
    n = m.index(max(m[:i]))
    res.append(n + 1)
    m = list(reversed(m[:n + 1])) + m[n + 1:]
    res.append(i)
    m = list(reversed(m))
    i -= 1
    m = m[:i]
res.remove(1)
print(res)              # res不要出现1
