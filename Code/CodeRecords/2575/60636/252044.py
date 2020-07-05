def maxDepthAfterSplit(seq):
    return [i & 1 ^ (seq[i] == ')') for i, c in enumerate(seq)]
seq=input()
print(maxDepthAfterSplit(seq))