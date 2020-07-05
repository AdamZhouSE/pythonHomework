n, ro = map(int, input().split(' '))
lch = [0] *1000
rch = [0] *1000
for i in range(0, n):
    t = list(int(n) for n in input().split(' '))
    w = t[0]
    lch[w] = t[1]
    rch[w] = t[2]
mid = []
ask = int(input())
stack = []
root = ro
while root or stack:
    while root:
        stack.append(root)
        root = lch[root]
    root = stack.pop()
    mid.append(root)
    root = rch[root]
mid.append(0)
if mid.index(ask) == len(mid):
    print(0)
else:
    print(mid[mid.index(ask)+1])