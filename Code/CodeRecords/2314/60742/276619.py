def preOrder(idxRoot):
    global l
    if left[idxRoot]!=0:
        idxL = roots.index(left[idxRoot])
        preOrder(idxL)
    l.append(roots[idxRoot])
    if right[idxRoot]!=0:
        idxR = roots.index(right[idxRoot])
        preOrder(idxR)
    return    

n = int(input())
l = []
roots = []
left = []
right = []
for t in range(n):
    s = [int(i) for i in input().split()]
    roots.append(s[0])
    left.append(s[1])
    right.append(s[2])
preOrder(0)
for i in range(len(l)):
    l[i] = str(l[i])
print(' '.join(l),end=' ')