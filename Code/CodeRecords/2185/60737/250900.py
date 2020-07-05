import math


t = int(input())
while t:
    n = int(input())
    digit = int(math.log(n+1, 2))
    order = int(n + 1 - math.pow(2, digit))
    b = [4] * digit
    times = 1
    while True:
        s = order // 2
        y = order % 2
        b[-times] = b[-times] + y*3
        if s == 0:
            break
        order = s
        times += 1
    b = [str(i) for i in b]
    print(''.join(b))
    t -= 1
  