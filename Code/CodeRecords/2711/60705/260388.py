def resemble(a: str, b:str) -> bool:
    c = []
    count = 0
    for i in range(0, len(b)):
        if a[i] == b[i]:
            c.append(0)
        else:
            c.append(1)
            count += 1
    if count == 0:
        return True
    if count == 2:
        j = c.index(1)
        k = c.index(1, j+1)
        if a[k] == b[j] and a[j] == b[k]:
            return True
    return False


def f(s:str) -> str:
    return s[1:-1]


if __name__ == '__main__':
    arr = list(map(f, input()[1:-1].split(",")))
    l = [[arr[0]]]
    for i in range(1, len(arr)):
        add = False
        for j in range(0, len(l)):
            for k in range(0, len(l[j])):
                if resemble(l[j][k], arr[i]):
                    l[j].append(arr[i])
                    add = True
        if not add:
            l.append([arr[i]])
    print(len(l))

