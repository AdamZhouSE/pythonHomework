num, root = map(int, input().split())
level = [[root]]
inorder = []
for x in range(num):
    fa,lch,rch = map(int, input().split())
    if fa not in inorder:
        inorder.append(fa)
    index = inorder.index(fa)
    if lch == 0 and rch == 0:
        continue
    elif lch == 0:
        inorder.insert(index + 1, rch)
    elif rch == 0:
        inorder.insert(index, lch)
    else:
        inorder.insert(index + 1, rch)
        inorder.insert(index, lch)

target = int(input())
index = inorder.index(target)
if index + 1 == len(inorder):
    print(0)
else:
    print(inorder[index + 1])