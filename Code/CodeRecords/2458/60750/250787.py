def dealTwo(num, a, b):
    tmp = []
    tmp_a = []
    for i in range(0, num):
        if a[i] in b:
            tmp_a.append(b.index(a[i]) + 1)
    length = 0
    for i in range(0, len(tmp_a)):
        if tmp == []:
            tmp.append(tmp_a[i])
            length = 1
        elif tmp_a[i] > tmp[len(tmp) - 1]:
            tmp.append(tmp_a[i])
            length += 1
        elif tmp_a[i] < tmp[0]:
            tmp[0] = tmp_a[i]
        else:
            for j in range(0, len(tmp) - 1):
                if tmp[j] < tmp_a[i] < tmp[j + 1]:
                    tmp[j + 1] = tmp_a[i]
    return length

def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    data = []
    res = 1

    for i in range(0,m):
        data.append(list(map(int,input().split(' '))))


    tmp = []
    for i in range(0,m - 1):
        for j in range(i + 1,m):
            tmp.append(dealTwo(n,data[i],data[j]))

    tmp.sort()

    print(tmp[0])


solve()





