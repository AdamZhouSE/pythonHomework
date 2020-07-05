def test():
    a = int(input())
    if a == 0:
        print(0)
        return

    b = bin(a)
    b = str(b)
    dist = 0
    max_dist = dist
    for i in range(0, len(b)):
        if b[i] == '1':
            break
    for k in range(i + 1, len(b)):
        dist = dist + 1
        if b[k] == '1':
            if max_dist < dist:
                max_dist = dist
            dist = 0

    print(max_dist)


test()