def isLike(s1, s2):
    diff = 0
    for x in range(len(s1)):
        if s1[x] != s2[x]:
            diff += 1
        if diff > 2:
            return 0
    return 1


def getRoot(root, i):
    if root[i] == i:
        return i
    else:
        return getRoot(root, root[i])

A = [x[1:-1] for x in input()[1:-1].split(",")]
root = {x : x for x in A}
for x in range(len(A)):
    for y in range(x):
        if not isLike(A[x], A[y]):
            continue
        root[getRoot(root, A[y])] = A[x]
count = 0
for x in A:
    if root[x] == x:
        count += 1
print(count)
