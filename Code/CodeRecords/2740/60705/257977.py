def func(time1, time2):
    time1 = list(map(int, time1[1:-1].split(":")))
    time2 = list(map(int, time2[1:-1].split(":")))
    time1 = time1[0] * 60 + time1[1]
    time2 = time2[0] * 60 + time2[1]
    if abs(time1 - time2) > 720:
        return 1440 - abs(time1 - time2)
    else:
        return abs(time1 - time2)


if __name__ == '__main__':
    l = input()[1:-1].split(",")
    m = 1440
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            delta = func(l[i], l[j])
            if delta < m:
                m = delta
    print(m)