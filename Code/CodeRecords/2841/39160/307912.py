from operator import or_, xor
import sys
 
n, m = map(int, input().split())
tree = [list(map(int, input().split()))]
for i in range(n):
    tree.append([(or_, xor)[i & 1](*tree[i][j: j + 2]) for j in range(0, len(tree[i]), 2)])

ans = []
for line in sys.stdin:
    p, b = line.split()
    p = int(p) - 1
    tree[0][p] = int(b)
    for j in range(n):
        p >>= 1
        tree[j + 1][p] = (or_, xor)[j & 1](*tree[j][p << 1: (p << 1) + 2])
    ans.append(str(tree[-1][0]))

print('\n'.join(ans))