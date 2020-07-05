def removeStones(stones):
    n = len(stones)
    global fmap
    fmap = [-1] * 20000
    for x, y in stones:
        union(x, y + 10000)
    return n - len({find(x) for x, y in stones})

def find(x):
    if fmap[x] == -1:
        return x
    else:
        return find(fmap[x])

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        fmap[px] = py

if __name__ == "__main__":
    data = [a for a in input().split("],[")]
    for i in range(len(data)):
        data[i] = [int(b) for b in data[i].strip("[]").split(',')]
    re = removeStones(data)
    print(re)