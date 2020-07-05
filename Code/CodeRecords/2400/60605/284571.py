
curridx = -1
resli = []
maxx = 1000000
liin = []


def build(cur: int, idx: int, newli: [int], lis: [int]):
    x = newli[idx]
    if x == -1:
        return
    lis[cur] += x
    build(cur-1, nextOne(), newli, lis)
    build(cur+1, nextOne(), newli, lis)
    return

def nextOne() -> int:
    global curridx
    curridx += 1
    return curridx

def ss(inpp: str) :
    global curridx, resli, maxx
    curridx = -1
    lis = [0 for j in range(maxx)]
    newli = []
    for j in inpp.strip().split():
        newli.append(int(j))
    build(maxx // 2, nextOne(), newli, lis)
    res = []
    for i in lis:
        if i != 0: res.append(str(i))
    return res
    # print()

if __name__ == '__main__':
    x = input().strip()
    maxx = 1000000
    while x != "-1":
        liin.append(x)
        try:
            x = input().strip()
        except EOFError:
            break

    res = []
    for i in liin:
        # print(i)
        res.append(ss(i))
    case = 1
    for i in res:
        print("Case " + str(case) + ":")
        print(" ".join(i))
        case += 1
        print()

