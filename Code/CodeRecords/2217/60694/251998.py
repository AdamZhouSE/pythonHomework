def func(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


p1 = list(map(int, input().split(",")))
p2 = list(map(int, input().split(",")))
p3 = list(map(int, input().split(",")))
p4 = list(map(int, input().split(",")))
l = [0] * 6
l[0], l[1], l[2], l[3], l[4], l[5] = func(p1, p2), func(p2, p3), func(p3, p4), func(p1, p3), func(p1, p4), func(p2, p4)
l.sort()
if len(set(l[0:4])) == 1 and len(set(l[4:])) == 1 and l[3] < l[4]:
    print(True)
else:
    print(False)
