n = int(input())
tree = input()
for i in range(1, n):
    subt = input()
    index = tree.find(subt[0])
    tree = tree[0:index]+subt+tree[index+1:]
for i in range(len(tree)):
    if tree[i]!='*':
        print(tree[i],end="")
