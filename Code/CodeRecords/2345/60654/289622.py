a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    d = 0
    num = 0
    for j in range(c.__len__() - 1, 0, -1):
        if j not in c:
            d = j
        else:
            c.remove(j)
    if d != 0:
        num = c[0]
    print(str(num) + " " + str(d))
