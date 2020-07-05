


def solve():
    m = int(input())
    n = int(input())
    k = int(input())
    data = []
    for i in range(0,m):
        for j in range(0,n):
            if i == 0:
                data.append(j+ 1)
            else:
                if j == 0:
                    data.append(i + 1)
                else:
                    data.append((i + 1) * (j + 1))
    data.sort()
    print(data[k - 1])

solve()


