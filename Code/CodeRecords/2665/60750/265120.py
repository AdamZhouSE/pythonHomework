


def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        line1 = list(map(int,input().split(' ')))
        x = line1[0]
        y = line1[1]
        z = line1[2]
        tmp = []
        x_goal = 0
        y_goal = 0

        for j in range(z,1,-1):
            if x % j == 0:
                x_goal += 1
                x = x - 1
            if y % j == 0:
                y_goal += 1
                y = y - 1
        tmp.append(x_goal)
        tmp.append(y_goal)
        res.append(tmp)

    for i in range(0,test):
        print(res[i][0],end = ' ')
        print(res[i][1])

solve()