from collections import Counter

m = sorted(list(input()))
count = Counter(m)
m.sort(key=count.get)
n = len(m) // 2
if m[-1] == m[n-1]:  # 最多的字符超过半数
    print("")
else:
    a, b = m[:n], m[n:]
    for i in range(len(b)):
        m[i * 2] = b[i]
    for i in range(len(a)):
        m[i * 2 + 1] = a[i]

    print(''.join(m))

