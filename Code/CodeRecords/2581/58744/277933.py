ghosts = []
row = int(input())
for i in range(row):
    ghosts.append(list(eval(input())))

target = list(eval(input()))


def escapeGhosts(ghosts, target):
    def taxi(P, Q):
        return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

    return all(taxi([0, 0], target) < taxi(ghost, target)
               for ghost in ghosts)


print(escapeGhosts(ghosts, target))
