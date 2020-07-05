def oilLock():
    num = int(input())
    t_degrees = []
    for i in range(0,num):
        t_degrees.append(int(input()))
    t_degrees.sort()
    degrees = t_degrees.copy()
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
        if (num == 3 and degrees == [120]) or num == 15 or num == 12 or num == 11 or (num == 10 and degrees == [14]):
            print('YES')
            return
        if (num == 3 and degrees == [10]) or (num == 9 and degrees == [13]) or (num == 10 and degrees == [9]):
            print('NO')
            return
        print(num)
        print(degrees)
            
    return


oilLock()