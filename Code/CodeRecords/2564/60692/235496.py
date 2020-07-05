a = input().split(",")
b = []
k = int(input())
x = int(input())
a.insert(1, a[0][1:])
a.remove(a[0])
a.insert(-1, a[-1][0:-1])
a.remove(a[-1])
ab = abs(x - int(a[0]))
pos = 0
for i in range(len(a)):
    a[i] = int(a[i])
    if abs(a[i] - x) < ab:
        pos = i
        ab = abs(a[i] - x)
if pos == 0:
    b = a[0:k]
elif pos == len(a)-1:
    b = a[len(a) - k: len(a)]
else:
    b.append(a[pos])
    k -= 1
    p = pos - 1
    q = pos + 1
    while k != 0:
        if p >= 0 and q <= len(a) - 1:
            if abs(a[p] - x) <= abs(a[q] - x):
                b.insert(0, a[p])
                p -= 1
                k -= 1
            else:
                b.append(a[q])
                q += 1
                k -= 1
        elif p < 0:
            b.append(a[q])
            q += 1
            k -= 1
        elif q > len(a) - 1:
            b.insert(0, a[p])
            p -= 1
            k -= 1
print(b)