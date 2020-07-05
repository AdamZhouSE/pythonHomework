def so(num):
    res = num - 1
    t = 1
    while t <num and 2 * t <= num:
        res += t
        t *= 2
    res += num - t
    return res
for i in range(0, eval(input())):
    num = eval(input())
    print(so(num))
