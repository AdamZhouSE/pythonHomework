def orz(a, b):
    res = ""
    for i in range(10):
        res = res + str(int(a[i]) or int(b[i]))
    return res


def solve(a, num):
    all_num = num.split(" ")
    t = len(all_num)
    i = 0
    while i < t:
        if int(int(all_num[i]) % int(a)) != 0:
            all_num.remove(all_num[i])
            t = len(all_num)
            i = i - 1
        i = i + 1
    binary = []
    for i in all_num:
        t = bin(int(i))[2:]
        while len(t) != 10:
            t = "0" + t
        binary.append(t)
    if len(binary) == 0:
        return 0
    else:
        res = binary.pop(0)
        while len(binary) != 0:
            res = orz(res,binary.pop(0))
        return int(res, 2)


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    eg = input().split(" ")
    num = input()
    result.append(solve(eg[1], num))
for i in result:
    print(i)
