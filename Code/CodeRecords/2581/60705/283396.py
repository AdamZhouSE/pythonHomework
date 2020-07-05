def escapeGhosts(ghosts, target):
    def taxi(P, Q):
        return abs(P[0] - Q[0]) + abs(P[1] - Q[1])
    return all(taxi([0, 0], target) < taxi(ghost, target) for ghost in ghosts)


if __name__ == '__main__':
    n = int(input())
    ghosts = []
    for i in range(0, n):
        ghosts.append(list(map(int, input().split(","))))
    target = list(map(int, input().split(",")))
    print(escapeGhosts(ghosts, target))
