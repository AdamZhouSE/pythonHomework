inp = int(input())
res = []
if inp <= 26:
    tmp = ord('A') + inp - 1
    print(chr(tmp))
else:
    n = inp
    while n > 26:
        n, reminder = divmod(n, 26)
        tmp = ord('A') + reminder - 1
        res.append(chr(tmp))
    tmp = ord('A') + n - 1
    res.append(chr(tmp))
    res.reverse()
    print(''.join(res))
