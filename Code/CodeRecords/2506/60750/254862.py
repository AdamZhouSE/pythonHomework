

def solve():
    tmp_a = list(map(int,input().split(',')))
    tmp = []
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

    print(length)

solve()