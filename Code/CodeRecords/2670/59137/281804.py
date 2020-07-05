def s3():
    t = int(input())
    for i in range(t):
        n = int(input())
        s0 = bin(n)
        s = ""
        for i in s0[2:]:
            if i == '0':
                s += '1'
            else:
                s += '0'
        print(int(s, 2))


s3()