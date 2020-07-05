def goals(player, guard):
    num_goals = 0
    while guard > 1:
        if player % guard == 0:
            player -= 1
            num_goals += 1
        else:
            guard -= 1
    return num_goals


count = int(input())
ans = []
for i in range(0, count):
    energy = input().split()
    p1 = int(energy[0])
    p2 = int(energy[1])
    grd = int(energy[2])
    scores = []
    scores.append(goals(p1, grd))
    scores.append(goals(p2, grd))
    ans.append(scores)
for exm in ans:
    print(exm[0], exm[1])
