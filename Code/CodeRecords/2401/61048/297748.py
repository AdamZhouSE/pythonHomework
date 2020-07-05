import math
def numop25() :
    label=int(input())
    l = int(math.log(label, 2)) + 1
    index = label - int(math.pow(2,l-1))
    res = [0] * l

    if (l % 2) == 0:
        index = (int(math.pow(2,l-1))- index - 1)

    for i in range(l, 0, -1):
        res[i - 1] = findlast(i, index)
        index =int(index/2)
    print(res)
    return 0


def findlast(l, cur):
    t = list(range(int(math.pow(2,l-1)), int(math.pow(2,l))))
    if (l % 2)==1:
        return t[cur]
    else:
        return t[(int(math.pow(2,l-1)) - cur - 1)]


numop25()
