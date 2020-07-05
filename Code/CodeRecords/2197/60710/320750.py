T = int(input())


def findNext(p, lists):
    if p + 1 ==len(lists) or p==len(lists):
        return 0
    else:
        return p + 1


for i in range(0, T):
    N = int(input())
    lists = []
    posi = 0

    for i in range(0, N):
        lists.append(i + 1)

    while len(lists) != 1:
        lists.remove(lists[findNext(posi, lists)])
        posi = findNext(posi, lists)

    print(str(lists[0]))