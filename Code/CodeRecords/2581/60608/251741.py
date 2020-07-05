def func31():
    ghosts = []
    for times in range(0, eval(input())):
        ghosts.append(eval(input()))
    target = eval(input())
    dist1 = abs(target[0]) + abs(target[1])
    dist2 = abs(ghosts[0][0] - target[0]) + abs(ghosts[0][1] - target[1])
    for i in range(1, len(ghosts)):
        dist2 = min(dist2, abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1]))
    print(dist1 < dist2)


func31()
