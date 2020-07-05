

def solve():
    line = sorted(list(map(int,input().split(','))))
    res = 0
    if len(line) == 0:
        print(res)
        return
    while line[0] != line[len(line) - 1]:
        for i in range(0,len(line) - 1):
            line[i] += 1
        res += 1
        line.sort()
    print(res)

solve()
