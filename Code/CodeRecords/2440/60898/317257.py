def notNum(l: list) -> int:
    l.sort()
    for i in range(len(l)):
        if l[i] != i :
            return i

n = list(map(int, input().strip().split(",")))
print(notNum(n))
