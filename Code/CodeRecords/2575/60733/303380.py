def maxDepthAfterSplit(seq):
    res = [0] * len(seq)
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            res[i] = 1 - res[i - 1]
        else:
            res[i] = res[i - 1]
    return res

seq = input()
res = maxDepthAfterSplit(seq)
print(res)

