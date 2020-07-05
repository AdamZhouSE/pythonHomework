def oilLock():
    num = int(input())
    degrees = []
    for i in range(0,num):
        degrees.append(int(input()))
    degrees.sort()
    while len(degrees) != 1:
        length = len(degrees)
        i = length - 1
        while i > 0:
            if degrees[i - 1] * degrees[i] <0:
                degrees[i - 1] = degrees[i] + degrees[i - 1]
            else:
                degrees[i - 1] = degrees[i] - degrees[i - 1]
            del degrees[i]
            i = i - 2
        degrees.sort()
    if degrees[0] == 0:
        print('YES')
    else:
        print('NO')
    return


oilLock()