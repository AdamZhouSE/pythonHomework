def func(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    var1 = x * y
    var2 = x % y
    while var2 != 0:
        x = y
        y = var2
        var2 = x % y
    var1 /= y
    #最小公倍数是var1， 最大公约数是y
    return var1


for test in range(0, int(input())):
    ls = list(map(int, input().split()))
    a, b, c, d = ls[0], ls[1], ls[2], ls[3]
    e = b // c - a // c + b // d - a // d - b // func(c, d) + a // func(c, d)
    print(int(e))