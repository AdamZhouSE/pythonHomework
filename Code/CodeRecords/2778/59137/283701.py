def s25():
    t = int(input())
    for i in range(t):
        s = input().split()
        l = int(s[0])
        r = int(s[1])

        count = 0
        for n in range(l, r+1):
            n = str(n)
            if n[0] == n[-1]:
                count += 1
        print(count)


s25()