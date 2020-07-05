import math
def findPath(label):
    if label == 0: return []
    if label == 1: return [1]
    res = [label]
    while label > 1:
        level = int(math.log2(label))
        level_start = 2 ** level
        remain = (label - level_start) // 2
        label = level_start - 1 - remain
        res.append(label)
    return res[::-1]

label = int(input())
print(findPath(label))