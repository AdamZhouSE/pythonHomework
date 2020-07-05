def escapeGhosts(ghosts, target):
    def taxi(P, Q):
        return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

    return all(taxi([0, 0], target) < taxi(ghost, target)
               for ghost in ghosts)
def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(",")];
    return nums;

k = int(input())
ghosts = []
for i in range(k):
    ghosts.append(getInput())
target = eval(input())
print(escapeGhosts(ghosts, target))