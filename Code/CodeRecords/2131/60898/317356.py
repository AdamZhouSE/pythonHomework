def isArray(l: list)-> bool :
    tmp, delta = 0, l[1] - l[0]
    for i in range(len(l) -1):
        if l[i+1] - l[i] != delta :
            return False
    return True


def strtoInt(s: str)-> int:
    return int(s)

def func(l: list) -> int:
    cnt = 0
    for i in range(len(l) -2):
        for j in range(2, len(l) - i):
            if isArray(l[i: i +j +1]) :
                cnt += 1
    return cnt

n = list(map(strtoInt, input().strip().split(",")))
print(func(n))