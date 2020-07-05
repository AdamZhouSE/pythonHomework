def D(source: str, target: str):
    if source.count(target) == 0:
        return "no exist\n"+source
    n = len(target)
    index = source.find(target)
    return source[0:index] + source[index + n:]


def I(source: str, a1: str, a2: str):
    if source.count(a1) == 0:
        return "no exist\n"+source
    index = source.rfind(a1)
    return source[0:index] + a2 + source[index:]


def R(source: str, a1: str, a2: str):
    if source.count(a1) == 0:
        return "no exist\n"+source
    return source.replace(a1, a2)


def func12():
    source = input()
    op = input().split()
    if op[0] == "D":
        print(D(source, op[1]))
    elif op[0] == "I":
        print(I(source, op[1], op[2]))
    else:
        print(R(source, op[1], op[2]))


func12()
