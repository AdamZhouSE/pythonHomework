# 12
def test():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    seqs = []
    for _ in range(0, k):
        seq = input().split()
        seq = list(map(int, seq))
        seqs.append(seq)
    max_len = 0
    for i in range(len(seqs[0]), -1, -1):
        if ok(seqs, i):
            print(i)
            return


def ok(seqs, i):
    if i == 0:
        return True
    else:
        seq = []
        seq0 = seqs[0]
        return dfs(seqs, seq0, seq, i, 0)


def dfs(seqs, seq0, seq, target, real):
    if real == target:
        return match(seq, seqs)
    else:
        copy_seq = seq.copy()
        for i in range(0, len(seq0) - target + real + 1):
            copy_seq.append(seq0[i])
            copy_seq0 = seq0[i:].copy()
            if dfs(seqs, copy_seq0, copy_seq, target, real + 1):
                return True
            copy_seq.pop()
        return False


def match(seq, seqs):
    for s in seqs:
        copy_seq = seq.copy()
        for i in range(0, len(s)):
            if len(copy_seq) == 0:
                break
            else:
                if s[i] == copy_seq[0]:
                    copy_seq.pop(0)
        if len(copy_seq) != 0:
            return False
    return True


test()
