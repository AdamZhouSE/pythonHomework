
curridx = -1

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

if __name__ == '__main__':
    liin = []
    x = input().strip()
    maxx = 1000000
    while x != "-1":
        liin.append(x)
        try:
            x = input().strip()
        except EOFError:
            break
    for i in range(len(liin)):
        curridx = -1
        lis = [0 for j in range(maxx)]
        newli = []
        for j in liin[i].strip().split():
            newli.append(int(j))
        build(maxx//2, nextOne(), newli, lis)
        print("Case", i+1, end="")
        print(":")
        for j in lis:
            if j != 0:
                print(j, end=" ")
        print()
