def union(li, set1, set2):
    if set1 == set2: return
    li[set1] += li[set2]
    li[set2] = set1

def find(li, start) -> int:
    while li[start] >= 0:
        start = li[start]
    return start

if __name__ == '__main__':
    originStr = input()
    li = list(eval(input()))
    liStr = list(originStr)
    newLi = [" " for i in range(len(originStr))]
    sets = [-1 for i in range(len(originStr))]

    for i in li:
        union(sets, find(sets, i[0]), find(sets, i[1]))
    liOfOrder = dict()

    for i in range(len(sets)):
        if sets[i] < 0:
            liOfOrder[i] = [i]
    for i in range(len(sets)):
        if sets[i] >= 0:
            liOfOrder[find(sets, i)].append(i)
    for i in liOfOrder.keys():
        liOfOrder[i].sort()
        currLi = []
        for j in liOfOrder[i]:
            currLi.append( liStr[j])
        currLi.sort()
        for j in range(len(liOfOrder[i])):
            newLi[liOfOrder[i][j]] = currLi[j]
    for i in newLi:
        print(i, end="")
    print()

