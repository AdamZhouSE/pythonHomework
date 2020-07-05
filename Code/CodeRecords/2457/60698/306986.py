# 11
def test():
    n = int(input())
    exps = []
    relations = [-1]*n
    for _ in range(0, n):
        exps.append(int(input()))
    for _ in range(0, n - 1):
        relation = input().split()
        relation = list(map(int, relation))
        relations[relation[0] - 1] = relation[1] - 1
    masters = []
    for i in range(0, len(relations)):
        if relations[i] == -1:
            masters.append(i)
    res = 0
    for master in masters:
        res = res + max(dfs(master, relations, exps, True), dfs(master, relations, exps, False))
    print(res, end='')


def dfs(master, relations, exps, masterGo):
    res = 0
    master_exp = exps[master]
    if masterGo:
        res = res + master_exp
        for i in range(0, len(relations)):
            if relations[i] == master:
                res = res + dfs(i, relations, exps, False)
    else:
        for i in range(0, len(relations)):
            if relations[i] == master:
                res = res + max(dfs(i, relations, exps, True), dfs(i, relations, exps, False))
    return res


test()