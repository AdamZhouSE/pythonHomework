def toB(n):
    res = ""
    while n > 0:
        if n % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
        n = n // 2
    return res


def func(n):
    flag = True
    for i in range(len(n)):
        if i % 2 == 1:
            if n[i] != '0':
                flag = False
        else:
            if n[i] != '1':
                flag = False
    return flag


t = int(input())
for i in range(t):
    n = int(input())
    res = []
    for j in range(1, n + 1):
        if func(toB(j)):
            res.append(j)
    for j in range(len(res) - 1):
        print(str(res[j]) + " ", end="")
    print(res[len(res) - 1])
