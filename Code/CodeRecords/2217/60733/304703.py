def validSquare(p1, p2, p3, p4):
    pl = [p1, p2, p3, p4]
    dist = []
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            l = (pl[i][1] - pl[j][1]) ** 2 + (pl[i][0] - pl[j][0]) ** 2
            dist.append(l)
    dist.sort()
    return True if dist[0] == dist[3] != 0 and dist[4] == dist[5] else False


p1 = list(map(int, input().split(",")))
p2 = list(map(int, input().split(",")))
p3 = list(map(int, input().split(",")))
p4 = list(map(int, input().split(",")))
print(validSquare(p1, p2, p3, p4))
