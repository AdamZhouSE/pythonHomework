n, ro = map(int, input().split(' '))
lch = [0] *1000
rch = [0] *1000
for i in range(0, n):
    t = list(int(n) for n in input().split(' '))
    w = t[0]
    lch[w] = t[1]
    rch[w] = t[2]
pre = []
mid = []
post = []

stack = []
root = ro
while root or stack:
    while root:
        pre.append(root)
        stack.append(root)
        root = lch[root]
    root = stack.pop()
    root = rch[root]

stack = []
root = ro
while root or stack:
    while root:
        stack.append(root)
        root = lch[root]
    root = stack.pop()
    mid.append(root)
    root = rch[root]

stack = []
root = ro
while root or stack:
    while root:
        stack.append(root)
        root = lch[root] if lch[root] is not 0 else rch[root]
    root = stack.pop()
    post.append(root)
    if len(stack) != 0 and lch[stack[-1]] == root:
        root = rch[stack[-1]]
    else:
        root = 0
#print(pre[0], end='')
for i in range(0, len(pre)):
#    print(' ', end='')
    print(pre[i], end=' ')
print()
#print(mid[0], end='')
for i in range(0, len(mid)):
#    print(' ', end='')
    print(mid[i], end=' ')
print()
print(post[0], end='')
for i in range(1, len(post)):
    print(' ', end='')
    print(post[i], end='')
print()