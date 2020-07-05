def s4():
    t = int(input())
    for i in range(t):
        n = int(input())
        s0 = bin(n)[2:]
        while len(s0) < 32:
            s0 = "0" + s0
        s = ""
        for i in s0:
            if i == '0':
                s += '1'
            else:
                s += '0'
        print(int(s, 2))


s4()