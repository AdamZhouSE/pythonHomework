n = eval(input())
nos = []
res = {}
for _ in range(n):
    s = input()
    nos.append(s)

cc = {
    'A': 2,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 3,
    'F': 3,
    'G': 4,
    'H': 4,
    'I': 4,
    'J': 5,
    'K': 5,
    'L': 5,
    'M': 6,
    'N': 6,
    'O': 6,
    'P': 7,
    'R': 7,
    'S': 7,
    'T': 8,
    'U': 8,
    'V': 8,
    'W': 9,
    'X': 9,
    'Y': 9,
}
for no in nos:
    r = []
    for c in no:
        if c.isnumeric():
            r.append(c)
        elif c.isalpha():
            r.append(cc[c])
    r = ''.join([str(x) for x in r[:3]]) + '-' + ''.join([str(x) for x in r[3:]])
    res[r] = res[r] + 1 if r in res else 1

res = [(k, v) for k, v in res.items() if v >= 2]
if not len(res):
    print('No duplicates.', end='')
for k, v in res:
    print(k, v, end='\n')
