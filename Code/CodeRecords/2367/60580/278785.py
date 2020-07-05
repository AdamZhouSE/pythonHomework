n = int(input())

if n % 2 == 0:
    print(-1)
else:
    length = -1
    for i in range(1, 20):
        l = []
        for j in range(i):
            l.append('1')
        s = "".join(l)
        testnum = int(s)

        if testnum % n == 0:
            s = str(testnum)
            length = len(s)
            break

    print(length)