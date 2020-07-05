n = int(input())
num = [int(x) for x in input().split()]
if n == 2:
    print(0)
else:
    a = max(num)
    num.remove(a)
    b = max(num)
    c = min(num)
    num.remove(c)
    d = min(num)
    print(min(a - d, b - c))

