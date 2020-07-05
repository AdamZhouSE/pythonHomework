a = input()
b = input()
res = 0
if len(a) == 1:
    res = b.count(a)
elif len(b) == 1:
    res = a.count(b)
else:
    for length in range(1, min(len(a), len(b))):
        for i in range(0, min(len(a), len(b)) - length + 1):
            if len(a) < len(b):
                tmp = ''.join(a[i:i + length])
                res += b.count(tmp)
            else:
                tmp = ''.join(b[i:i + length])
                res += a.count(tmp)
print(res)
