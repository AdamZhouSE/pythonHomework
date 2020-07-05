def convert_to_10(x: str, n: int):
    tmp = list(x[:])
    tmp.reverse()
    res = 0
    for i in range(0, len(x)):
        res += int(tmp[i]) * int(pow(n, i))
    return res


def ten_to_3(x: int):
    res = []
    while x >= 3:
        res.append(str(x % 3))
        x = x // 3
    res.append(str(x))
    res.reverse()
    return ''.join(res)


def check(x, y):
    if len(x) != len(y):
        return False
    else:
        con = 1
        for i in range(len(x)):
            if x[i] != y[i]:
                con -= 1
        if con != 0:
            return False
        else:
            return True


a = input()
b = input()
for i in range(len(a)):
    tmp = a[:i] + str(int(a[i]) ^ 1) + a[i + 1:]
    ox = convert_to_10(tmp, 2)
    th = ten_to_3(ox)
    if check(th, b):
        print(ox,end='')
        break
