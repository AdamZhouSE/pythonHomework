from math import sqrt


def test():
    k = int(input())
    circles = []
    while True:
        x = int((1 + sqrt(1 + 8 * k)) // 2)
        c2_x = comb2(x)
        k = k - comb2(x)
        circles.append(x)
        if k <= 0:
            break
    note=sum(circles)
    e=note+len(circles)-1
    print(note,e)
    i = 1
    links = []
    for j in circles:
        for l in range(0, j - 1):
            print(str(i + l) + ' ' + str(i + l + 1))
        print(str(i + j - 1) + ' ' + str(i))
        if i != 1:
            links.append([1, i+j-1])
        i = i + j
    for link in links:
        print(str(link[0]) + ' ' + str(link[1]))


def comb2(x):
    if x <= 1:
        return 0
    else:
        return int((x * (x - 1)) // 2)


test()
