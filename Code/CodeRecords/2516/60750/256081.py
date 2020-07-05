

def solve():
    n = int(input())
    data = []
    for i in range(0,n):
        data.append(list(map(int,input().split(','))))

    res = []
    for i in range(0,n):
        left = []
        index = []
        for j in range(0,n):
            if data[j][0] > data[i][1]:
                left.append(data[j][0])
                index.append(j)
            elif data[j][0] == data[i][1]:
                left.append(data[j][0])
                res.append(j)
                break
        if len(left) == 0:
            res.append(-1)

    print(res)

solve()

