num = int(input().strip())
res = []
for i in range(num):
    root,left,right = [i for i in input().strip()]
    if root in res:
        index = res.index(root)
    else:
        if root != '*':
            res.append(root)
        if left != '*':
            res.append(left)
        if right != '*':
            res.append(right)
        continue
    if right != '*':
        res.insert(index+1,right)
    if left != '*':
        res.insert(index+1,left)
print("".join(res),end="")