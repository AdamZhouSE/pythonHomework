def c(a, b):
    up = 1
    t = int(b)
    for i in range(int(b) - int(a)):
        up = up * t
        t = t - 1
    down = 1
    for i in range(1, int(b) - int(a) + 1):
        down = down * i
    return int(up / down)


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    res = 1
    for i in range(1, int((num + 1) / 2) + 1):
        res = res + c(i, num + 1 - i)
    result.append(pow(2, num) - res)
for i in result:
    print(i)