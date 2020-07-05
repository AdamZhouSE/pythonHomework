size = int(input())
for i in range(size):
    x = input()
    aT = input().split()
    a = []
    for var in aT:
        a.append(int(var))
    bT = input().split()
    b = []
    for var in bT:
        b.append(int(var))
    j = 0
    result = []
    while j < len(a):
        temp = []
        k = 0
        while k < j:
            temp.append(0)
            k += 1
        for var in b:
            temp.append(a[j] * var)
        z = 0
        while z < len(result):
            temp[z] += result[z]
            z += 1
        result = temp
        j += 1
    lw = ''
    zzz = 0
    while zzz < len(result):
        if zzz == len(result) - 1:
            lw += str(result[zzz])
        else:
            lw += str(result[zzz]) + " "
        zzz += 1
    print(lw)
