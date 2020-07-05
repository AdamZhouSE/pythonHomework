import math
def isInt(fl: float)-> bool:
    a = float(int(fl))
    if a == fl :
        return True
    return False

def strtoInt(string:str)-> int:
    return int(string)

def func(l: list) -> int:
    l.sort()
    for i in range(len(l))[::-1]:
        if l[i] < 0:
            return -1
        if isInt(math.sqrt(l[i])) == False:
            return l[i]


n = int(input())
l = list(map(strtoInt, input().strip().split(" ")))
print(func(l))