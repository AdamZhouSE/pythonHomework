def so(lis, length, depth, res, zzz):
    if depth == length and zzz.count('a') * zzz.count('b') * zzz.count('c') > 0:
        res[0] += 1
    elif depth < length:
        so(lis, length, depth + 1, res, zzz)
        if zzz and zzz[-1] == 'c' and lis[depth] != 'c':
            a=0
        elif zzz and zzz[-1] == 'b' and lis[depth] == 'a':
            a=0
        else:
            so(lis, length, depth + 1, res, zzz + [lis[depth]])


for _ in range(0, eval(input())):
    lis, res = list(input()), [0]
    so(lis, len(lis), 0, res, [])
    print(res[0])