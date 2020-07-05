import re


ord = list()
def order_(root):
    if root == 0:
        return
    else:
        order_(res[root][0])
        ord.append(root)
        order_(res[root][1])


pattern = re.compile('[0-9]+')
a = pattern.findall(input())
n, root = int(a[0]), int(a[1])
res = [[0, 0] for _ in range(2*n+5)]
for i in range(n):
    a = [int(x) for x in pattern.findall(input())]
    fa, lch, rch = a[0], a[1], a[2]
    res[fa] = [lch, rch]

order_(root)
find = int(input())
try:
    print(ord[ord.index(find) + 1])
except IndexError:
    print(0)


