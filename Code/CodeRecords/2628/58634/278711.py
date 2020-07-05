def gcd(x, y):
    if not y:
        return x
    return gcd(y, x % y)


t = int(input())
for i in range(t):
    x1, y1 = map(int, input().split(" "))
    x2, y2 = map(int, input().split(" "))
    x3, y3 = map(int, input().split(" "))
    a1 = x2 - x1
    b1 = y2 - y1
    a2 = x3 - x1
    b2 = y3 - y1
    area = abs(a1 * b2 - a2 * b1)  # x乘算面积
    num = 0
    num += gcd(abs(x1 - x2), abs(y1 - y2))
    num += gcd(abs(x2 - x3), abs(y2 - y3))
    num += gcd(abs(x3 - x1), abs(y3 - y1))
    print((area-num)//2+1)

