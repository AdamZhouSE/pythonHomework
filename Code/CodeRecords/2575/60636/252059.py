def maxDepthAfterSplit(seq):
    res = [0] * len(seq)
    for i, c in enumerate(seq):
        if c == '(':
            res[i] = i & 1
        else:
            res[i] = 1 - (i & 1)
    return res
seq=input()
print(maxDepthAfterSplit(seq))