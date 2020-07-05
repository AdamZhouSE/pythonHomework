s = input()
flag, r = False, 0
values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
res = []
for x in s:
    if (x == 'V' or x == 'X') and res.count(1) > 0:
        res.remove(1)
        res.append(-1)
    if (x == 'L' or x == 'C') and res.count(10) > 0:
        res.remove(10)
        res.append(-10)
    if (x == 'D' or x == 'M') and res.count(100) > 0:
        res.remove(100)
        res.append(-100)
    res.append(values[x])

print(sum(res))
