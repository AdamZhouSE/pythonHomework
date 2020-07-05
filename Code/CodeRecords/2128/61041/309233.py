def rotate(l: list) -> int:
    cnt, tmp = 0, 0
    for i in l:
        tmp += cnt * i
        cnt += 1
    return tmp

def strtoInt(s: str)-> int:
    return int(s)

def findNumber(l: list) -> int:
    n = []
    for i in range(len(l)):
        n.append(rotate(l))
        tmp = l[:-1]
        s = l[-1]
        l = tmp
        l.insert(0, s)
    n.sort()
    return n[-1]

n = list(map(strtoInt, input().strip().split(",")))
print(findNumber(n))
