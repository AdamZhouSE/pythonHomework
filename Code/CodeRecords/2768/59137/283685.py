def s18():
    t = int(input())
    for i in range(t):
        s = input().split()
        a = int(s[0])
        b = int(s[1])
        c = int(s[2])

        count = 0
        for j in range(a, b+1):
            if j % c == 0:
                count += 1
        print(count)


s18()