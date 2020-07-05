def judge():
    if n <= 2:
        return 'YES'
    lst = []
    idx_1 = bi.index(max(bi))
    bi_c = bi.copy()
    bi_c.pop(idx_1)
    idx_2 = bi.index(max(bi_c))
    total = bi[idx_1] - ai[idx_1] + bi[idx_2] - ai[idx_2]
    return 'YES' if total >= sum(ai) - ai[idx_1] - ai[idx_2] else 'NO'


n = int(input())
ai, bi = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
print(judge())
