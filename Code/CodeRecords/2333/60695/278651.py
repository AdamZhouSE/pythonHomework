import math

x = int(input())
y = int(input())
bound = int(input())
if bound < 2:
    print("[]")
else:
    res = set()
    xi = int(math.log(bound - 1, x)) if x != 1 else 0
    yj = int(math.log(bound - 1, y)) if y != 1 else 0
    for i in range(xi + 1):
        for j in range(yj + 1):
            tmp = x ** i + y ** j
            if tmp <= bound:
                res.add(tmp)
    a = list(res)
    print(a)