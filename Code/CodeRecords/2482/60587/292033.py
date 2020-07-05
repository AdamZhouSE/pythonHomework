T = int(input())
while T > 0:
    T -= 1
    s = int(input())
    m = int(input())
    if s % m == 0:
        print(int(s / m))
    else:
        tmp = str(s / m)
        # print(tmp[2])
        if len(tmp) > 3:
            if tmp[2] == tmp[3]:
                res = tmp[0] + '.' + '(' + tmp[2] + ')'
                print(res)
        else:
            print(s / m)
