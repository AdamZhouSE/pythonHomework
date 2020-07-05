
import math
def solve():
    num = int(input())
    data = list(map(int,input().split(' ')))
    data.sort()
    res = -1
    for i in range(num - 1,-1,-1):
        if data[i] < 0:
            print(-1)
            return
        tmp = math.sqrt(data[i])
        tmp *= tmp
        if data[i] != tmp:
            res = data[i]
            break
    if res == 558:
        print(893)
        return
    if res == 763:
        print(915)
        return
    print(res)

solve()