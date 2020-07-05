def merge(a):
    ok = True
    for i in a:
        for j in a:
            if i == j:
                continue
            else:
                if i[0] < i[1] < j[0] < j[1] or j[0] < j[1] < i[0] < i[1]:
                    continue
                else:
                    ok = False
                    a.remove(i)
                    a.remove(j)
                    result = [min(i[0], j[0]), max(i[1], j[1])]
                    a.append(result)
                    break
        if not ok:
            break
    if not ok:
        merge(a)
    if ok:
        a.sort(key=lambda x: x[0])
        print(a)


if __name__ == '__main__':
    a = eval(input())
    merge(a)
