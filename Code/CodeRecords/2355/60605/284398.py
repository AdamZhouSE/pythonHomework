
def sso(n: int, m: int) -> int:
    minS = 99999999999
    x = input().strip().split()
    weights = []
    for i in x:
        weights.append(int(i))

    sides = []
    conj_sides = [[] for i in range(n)]
    for i in range(m):
        x = input().strip().split()
        sides.append([int(x[0]) - 1, int(x[1]) - 1])
        conj_sides[int(x[0]) - 1].append(int(x[1]) - 1)
        conj_sides[int(x[1]) - 1].append(int(x[0]) - 1)
    # print(conj_sides)
    for i in sides:
        a = i[0]
        b = i[1]
        minS = min(minS, solve(conj_sides, weights, a, b))
    return minS



def solve(conj_sides: [[int]], weights: [int], a: int, b: int) -> int:
    # print(a, b)
    tota = 0
    visited = [a]
    queue0 = [a]
    while len(queue0) > 0:
        t = queue0.pop(0)
        tota += weights[t]
        for i in conj_sides[t]:
            if i not in visited and i != b:
                visited.append(i)
                queue0.append(i)
    # print("visited", visited)
    totb = 0
    queue0 = [b]
    visited = [b]
    while len(queue0) > 0:
        t = queue0.pop(0)
        totb += weights[t]
        for i in conj_sides[t]:
            if i not in visited and i != a:
                visited.append(i)
                queue0.append(i)
    # print("visited", visited)
    return abs(tota-totb)

if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0])
    m = int(x[1])
    res = []
    while n != 0 and m != 0:
        res.append(sso(n, m))
        x = input().strip().split()
        n = int(x[0])
        m = int(x[1])
    for i in range(len(res)):
        print("Case "+str(i+1)+":", res[i])