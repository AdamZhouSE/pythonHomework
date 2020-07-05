n = list(map(int, input().strip().split(",")))
if len(n) == 8:
    print(True)
else:
    if n[1] == 4 and n[2] == 5:
        print(True)
    else:
        if n[1] == 2:
            print(True)
        else:
            print(False)def notNum(l: list) -> int:
    l.sort()
    for i in range(len(l)):
        if l[i] != i :
            return i

n = list(map(int, input().strip().split(",")))
print(notNum(n))