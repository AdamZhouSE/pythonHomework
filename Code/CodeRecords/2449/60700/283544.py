def search(l: list, s: str):
    if s >= l[0]:
        return binarySearch(l[0: l.index(max(l))], s)
    else:
        return binarySearch(l[l.index(min(l)): len(l)-1], s)+l.index(min(l))


def binarySearch(l: list, s: str):
    index = -1
    lp = 0
    rp = len(l)-1
    while True:
        t = (lp + rp) // 2
        if s == l[t]:
            index = t
            break
        if s > l[t]:
            lp = t
        if s < l[t]:
            rp = t
        if lp == rp:
            break
    return index


line = input()
s = input()
l = line.split(',')
if s >= l[0]:
    print(binarySearch(l[0: l.index(max(l))], s))
else:
    print(binarySearch(l[l.index(min(l)): len(l) - 1], s) + l.index(min(l)))
