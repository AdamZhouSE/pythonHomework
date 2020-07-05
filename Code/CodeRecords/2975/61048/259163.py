def strop1():
    inp=list(input())
    inp=sorted(inp)
    s = ""
    for item in inp:
        s = s + str(item)
    print(s)
    return

strop1()