t = int(input())
res = []
for i in range(t):
    n = int(input())
    st = bin(n).replace('0b', '')
    length = len(st) - 1
    if list(st).count('1') == 1:
        while length >= 0:
            if st[length] == '1':
                res.append(len(st) - length)
            length -= 1
    else:
        res.append(-1)

for i in res:
    print(i)