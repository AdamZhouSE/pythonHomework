


def solve():
    a = sorted(list(map(int,input().split(','))))
    b = sorted(list(map(int,input().split(','))))
    c = sorted(list(map(int,input().split(','))))
    d = sorted(list(map(int,input().split(','))))
    res = 0

    for i in range(0,len(a)):
        for j in range(0,len(a)):
            for k in range(0,len(a)):
                for m in range(0,len(a)):
                    s = a[i] + b[j] + c[k] + d[m]
                    if s == 0:
                        res += 1
                    elif s > 0:
                        break



    print(res)

solve()
