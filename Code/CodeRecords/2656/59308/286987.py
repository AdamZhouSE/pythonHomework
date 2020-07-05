T = int(input())
for _ in range(T):
    __ = [int(x) for x in input().split(' ')]
    a, b = __[0], __[1]
    res_ = []
    res__ = []
    while a > 0:
        res_.append(a%2)
        a//=2
    while b > 0:
        res__.append(b%2)
        b//=2
    flag = -1
    for i in range(max(len(res_),len(res__))):
        try:
            if res_[i] != res__[i]:
                flag = i + 1
                break
        except IndexError:
            flag = i
    print(flag)
