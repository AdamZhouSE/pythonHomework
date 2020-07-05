a = int(input())
for i in range(a):
    b = int(input())
    sn = 3
    s1 = 1
    s0 = 2
    if b == 0:
        sn = s0
    elif b == 1:
        sn = s1
    else:
        for j in range(b-1):
            sn = s1 + s0
            s0 = s1
            s1 = sn
    print(sn % 1000000007)
