

def solve():
    a = list(map(int,input().split(',')))
    f = []
    for k in range(0,len(a)):
        if k == 0:
            b = a.copy()
        elif k == len(a) - 1:
            b = a[1:] + a[0:]
        else:
            b = a[len(a) - k:] + a[:len(a) - k]
        tmp = 0
        for j in range(0,len(a)):
            tmp += j * b[j]
        f.append(tmp)

    f.sort(reverse=True)
    print(f[0])

solve()