def escapeGhosts(ghosts, target):
    def taxi(P, Q):
        return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

    return all(taxi([0, 0], target) < taxi(ghost, target) for ghost in ghosts)

size = int(input())
ghosts = []
while size > 0:
    size -= 1
    temp = [int(x) for x in input().split(",")]
    ghosts.append(temp)
target = [int(x) for x in input().split(",")]
print(escapeGhosts(ghosts, target))
