def pushAllSons(weights: [int], liSon: [set], father: int, a: int) :
    queue = []
    queue.append(father)
    while len(queue) > 0:
        cur = queue.pop(0)
        for i in liSon[cur]:
            queue.append(i)
        weights[cur] += a

def queryTotWeight(weights: [int], liFather: [int], froo: int) -> int:
    cur = froo
    tot = 0
    while froo != -1:
        tot += weights[froo]
        froo = liFather[froo]
    return tot

if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0])
    m = int(x[1])
    weights = []
    x = input().strip().split()
    liFather = [-1 for i in range(n)]
    liSon = [set() for i in range(n)]
    for i in x:
        weights.append(int(i))
    for i in range(n-1):
        x = input().strip().split()
        fro = int(x[0])
        too = int(x[1])
        liFather[too-1] = (fro-1)
        liSon[fro-1].add(too-1)
    ops = []
    for i in range(m):
        ops.append(input().strip().split())
    for op in ops:
        if op[0] == "1":
            weights[int(op[1])-1] += int(op[2])
        elif op[0] == "2":
            pushAllSons(weights, liSon, int(op[1])-1, int(op[2]))
        else:
            print(queryTotWeight(weights, liFather, int(op[1])-1))
    # print(liFather)
    # print(liSon)