n = int(input())

if n % 2 == 0:
    print(-1)
else:
    for i in range(1, 20):
        l = []
        for j in range(i):
            l.append('1')
        s = "".join(l)
        testnum = int(s)

        if testnum % n == 0:
            break
    s = str(testnum)
    print(testnum)
    print(len(s))


