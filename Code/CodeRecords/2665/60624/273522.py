def func22():
    t = int(input())
    while t > 0:
        t -= 1
        players = list(map(int, input().split(" ")))
        x, y, z = players[0], players[1], players[2]
        res = [0,0]
        while z != 1:
            if x % z == 0:
                res[0] += 1
                x -= 1
            if y % z == 0:
                res[1] += 1
                y -= 1
            z -= 1
        print(res[0],end=" ")
        print(res[1])
    return
func22()